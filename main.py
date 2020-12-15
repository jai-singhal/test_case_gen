from ABC import ABC_Algorithm
from model.test_suite import TestSuite
from program.even_odd import EvenOddProgram
from program.quadratic_eqn import QuadraticEquationProgram
from program.remainder import RemainderProgram

import math
import os
import time
from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', response="")

@app.route('/api/post/run', methods=['POST'])
def run_program():
    program_instance = None
    choice = request.form["choice"]
    print(choice)
    if choice == "1":
        program_instance = EvenOddProgram()
    elif choice == "2":
        program_instance = QuadraticEquationProgram()
    elif choice == "3":
        program_instance = RemainderProgram()
    else:
        return jsonify({"success": False, "error": "No program selected", "status_code": 400})

    instance = ABC_Algorithm()
    tick = time.time()
    controlFlowPaths = instance.get_cf_paths(program_instance)
    testSuite = instance.test_suite_gen(controlFlowPaths, program_instance)
    tock = time.time()
    response = {
        "path_fitness": [],
        "time_taken": tock-tick
    }

    for path in controlFlowPaths.getPaths():
        path_res = {}
        path_res["fitness"] = path.fitness_value
        path_res["path"] = []
        for node in path.getNodes():
            path_res["path"].append({
                "node": node.lineNumber,
                "fitness": node.fitness,
            })
            
        if path_res not in response["path_fitness"]:
            response["path_fitness"].append(path_res)

    return jsonify({
        "success": True,
        "response": response,
        "status_code": 200
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)