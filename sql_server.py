import os
import sqlite3
import json
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

DB_FILE = "vaibhav.db"
PORT = 8000

def init_db():
    """Initializes the SQLite database with tables matching the student's Pandas practice data."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create Employees Table
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("""
        CREATE TABLE employees (
            Employee TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary INTEGER NOT NULL,
            Experience INTEGER NOT NULL,
            City TEXT NOT NULL
        );
    """)
    employees_data = [
        ('Amit', 'IT', 75000, 5, 'Delhi'),
        ('Sara', 'HR', 45000, 3, 'Mumbai'),
        ('Raj', 'IT', 85000, 7, 'Delhi'),
        ('Priya', 'Finance', 60000, 4, 'Bangalore'),
        ('Karan', 'HR', 50000, 2, 'Mumbai'),
        ('Neha', 'IT', 70000, 6, 'Delhi'),
        ('Vikas', 'Finance', 65000, 5, 'Bangalore'),
        ('Pooja', 'HR', 48000, 3, 'Mumbai')
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?);", employees_data)

    # Create Students Table
    cursor.execute("DROP TABLE IF EXISTS students;")
    cursor.execute("""
        CREATE TABLE students (
            Student TEXT NOT NULL,
            Maths INTEGER NOT NULL,
            Science INTEGER NOT NULL,
            Attendance INTEGER NOT NULL
        );
    """)
    students_data = [
        ('Vaibhav', 72, 68, 90),
        ('Rahul', 35, 72, 60),
        ('Priya', 85, 90, 95),
        ('Ankit', 45, 38, 40),
        ('Neha', 90, 88, 85)
    ]
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?);", students_data)

    # Create Movies Table
    cursor.execute("DROP TABLE IF EXISTS movies;")
    cursor.execute("""
        CREATE TABLE movies (
            Title TEXT NOT NULL,
            Year INTEGER NOT NULL,
            Rating REAL NOT NULL,
            Genre TEXT NOT NULL
        );
    """)
    movies_data = [
        ('Inception', 2010, 8.8, 'Sci-Fi'),
        ('The Dark Knight', 2008, 9.0, 'Action'),
        ('Titanic', 1997, 7.9, 'Romance/Drama'),
        ('Interstellar', 2014, 8.7, 'Sci-Fi'),
        ('Cars', 2006, 7.2, 'Animation'),
        ('Avengers: Endgame', 2019, 8.4, 'Action/Sci-Fi')
    ]
    cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?);", movies_data)

    conn.commit()
    conn.close()
    print("Database initialized successfully with tables: employees, students, movies.")

class SQLTutorRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Silence default request logging to avoid cluttered output, but keep errors
        pass

    def do_GET(self):
        # Serve index.html as the root
        if self.path == "/" or self.path == "/index.html":
            self.path = "/sql_tutor.html"
        return super().do_GET()

    def do_POST(self):
        if self.path == "/query":
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                query = data.get('query', '').strip()
                
                # Execute the query
                result = self.execute_sql(query)
                
                # Send JSON response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
                
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def execute_sql(self, query):
        if not query:
            return {"success": False, "error": "Query is empty."}
            
        # Protect against destructive operations (optional, but good practice for tutor)
        lower_query = query.lower()
        forbidden_keywords = ["drop database", "alter database", "vacuum", "attach"]
        for keyword in forbidden_keywords:
            if keyword in lower_query:
                return {"success": False, "error": f"Operation not allowed: {keyword}"}
                
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        try:
            cursor.execute(query)
            
            # Check if it was a SELECT query or other
            if cursor.description:
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                results_list = [dict(row) for row in rows]
                
                conn.commit()
                return {
                    "success": True,
                    "type": "select",
                    "columns": columns,
                    "data": results_list,
                    "rowCount": len(results_list)
                }
            else:
                conn.commit()
                affected = cursor.rowcount
                return {
                    "success": True,
                    "type": "write",
                    "rowCount": affected,
                    "message": f"Query executed successfully. Rows affected: {affected if affected >= 0 else 0}"
                }
        except sqlite3.Error as e:
            return {"success": False, "error": str(e)}
        finally:
            conn.close()

def run_server():
    init_db()
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SQLTutorRequestHandler)
    print(f"\n=======================================================")
    print(f"  SQL TUTOR SERVER IS ACTIVE!")
    print(f"  Open your browser to: http://localhost:{PORT}")
    print(f"  Press Ctrl+C in this terminal to stop the server.")
    print(f"=======================================================\n")
    
    # Automatically open standard browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping SQL Tutor Server...")
        httpd.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    run_server()
