from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def validate_matrix(matrix_data, rows, cols, suffix=''):
    try:
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                key = f'matrix{i}{j}{suffix}'
                value = float(matrix_data.get(key, 0))
                row.append(value)
            matrix.append(row)
        return np.array(matrix)
    except (ValueError, TypeError):
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    rows = int(request.form.get('rows', 2))
    cols = int(request.form.get('cols', 2))
    
    if request.method == 'POST':
        operation = request.form.get('operation')
        
        if operation:
            # Validate both matrices
            matrix1 = validate_matrix(request.form, rows, cols, '')
            matrix2 = validate_matrix(request.form, rows, cols, '2')
            
            if matrix1 is None or matrix2 is None:
                return render_template('index.html', error="Invalid matrix input", 
                                       rows=rows, cols=cols)
            
            try:
                if operation == 'add':
                    result = np.add(matrix1, matrix2)
                elif operation == 'subtract':
                    result = np.subtract(matrix1, matrix2)
                elif operation == 'multiply':
                    # Check if matrices can be multiplied
                    if matrix1.shape[1] != matrix2.shape[0]:
                        return render_template('index.html', 
                                               error="Matrix dimensions incompatible for multiplication",
                                               rows=rows, cols=cols)
                    result = np.matmul(matrix1, matrix2)
                
                return render_template('index.html', 
                                       result=result.tolist(),
                                       rows=rows, cols=cols,
                                       matrix1=matrix1.tolist(),
                                       matrix2=matrix2.tolist())
            except Exception as e:
                return render_template('index.html', 
                                       error=f"Operation failed: {str(e)}",
                                       rows=rows, cols=cols)
    
    return render_template('index.html', rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)
