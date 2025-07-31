import math
import sys
import time
from decimal import *

# Try to import turtle, but fall back to command-line mode if not available
try:
    import turtle
    from turtle import *
    from turtle import Screen
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

try:
    from pi_analysis import calculate_pi_estimate, calculate_efficiency_metrics, compare_accuracy_vs_time, analyze_accuracy_time_relationship, find_optimal_trade_off
    ANALYSIS_AVAILABLE = True
except ImportError:
    ANALYSIS_AVAILABLE = False
    print("Warning: pi_analysis module not available. Some features may be limited.")

px2cm = 0.0264583333

#COLOUR CONSTANTS
BG = "#1D4A5D"
POLYGON = "#C26ED1"
CIRCLE = "#531D5D"
TEXT = "#1FFFC7"
DOT = "#1B0C1D"

rendering = False

# Initialize GUI components only if available
if GUI_AVAILABLE:
    mode("logo")
    title("Pi Estimation and Visualization")
    screen = Screen()
    screen.setup(720, 720)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    turtle.bgcolor(BG)

def init(setN=False):
    global n, r, angle
    if setN is not False and setN >= 3:
        n = setN
    else:
        n = 3
    r = 150
    angle = 360 / n


def askN():
    n = turtle.textinput("Enter the number of sides:", "Number of sides on polygon: ")
    execMain(True, int(n))

def getPositions(_angle, _n, _r):
    _positions = []
    t.penup()
    t.setheading(0 - angle)
    for side in range(_n):
        t.goto(0, 0)
        t.forward(_r)
        t.right(_angle)
        _positions.append(t.pos())
    return  _positions


def calculateAreas(polySideLength):
    A = angle / 2
    polygonApothem = r * math.cos(math.radians(A))
    polygonArea = n * ((polySideLength * polygonApothem) / 2)
    piEstimate = polygonArea / (r ** 2)
    _areaInfo = {"actual circle area": (Decimal((math.pi * (r ** 2)))) * Decimal(px2cm) ** 2,  # pi * radius squared
                 "polygon area": (Decimal(polygonArea)) * Decimal(px2cm) ** 2,
                 "pi estimate": Decimal(piEstimate)}
    _areaInfo["pi error"] = Decimal(math.pi) - _areaInfo["pi estimate"]
    
    # Add efficiency analysis if analysis module is available
    try:
        pi_error_float = float(_areaInfo["pi error"])
        pi_accuracy = 1 - (pi_error_float / math.pi)
        calculation_time = time.time() - getattr(calculateAreas, 'start_time', time.time())
        
        efficiency_metrics = calculate_efficiency_metrics({
            'pi_accuracy': pi_accuracy,
            'calculation_time': max(calculation_time, 1e-6),  # Prevent division by zero
            'pi_error': pi_error_float
        })
        
        _areaInfo["pi accuracy"] = Decimal(pi_accuracy)
        _areaInfo["efficiency score"] = Decimal(efficiency_metrics['efficiency_score'])
        _areaInfo["accuracy per second"] = Decimal(efficiency_metrics['accuracy_per_second'])
    except (NameError, Exception):
        # Analysis module not available or error occurred
        pass
    
    return _areaInfo


def drawVizualization():
    global rendering
    startTime = time.time()
    calculateAreas.start_time = startTime  # Store start time for efficiency calculation
    rendering = True
    t.penup()
    t.clear()
    t.goto(0,0)
    t.color(TEXT)
    t.write("Loading...", move=False, align="center", font=("Arial", 50, "bold"))
    info = getPositions(angle, n, r)
    # render circle
    t.clear()
    t.color(CIRCLE)
    t.begin_fill()
    t.goto((0 + r), 0)
    t.setheading(0)
    t.pendown()
    t.circle(r)
    t.end_fill()
    t.penup()
    # render polygon
    positions = info
    start = positions[0]
    t.penup()
    t.goto(start[0], start[1])
    t.begin_poly()
    t.color(POLYGON)
    t.begin_fill()
    for pos in positions:
        t.pendown()
        t.goto(pos[0], pos[1])
    s = t.distance(start[0], start[1])
    t.goto(start[0], start[1])
    t.end_poly()
    polygon = t.get_poly()
    turtle.register_shape("polygon", polygon)
    t.end_fill()
    t.penup()
    # render text
    t.color(TEXT)
    t.goto(0, -300)
    t.write("Don't spam the controls!"
            "\nPress R to reset. "
            "\nPress Q to quit. "
            "\nPress E to enter number of sides. "
            "\nPress A to analyze accuracy vs time."
            "\nLeft-Click to increase the number of sides."
            "\nRight-Click to decrease the number of sides.",
            False, align="center", font=("Arial", 12, "normal"))
    areaInfo = calculateAreas(s)
    t.goto(-300, 300)
    t.setheading(0)
    spacing = 20
    t.color(CIRCLE)
    t.write("Actual Area (area of circle using pi): " + str(areaInfo["actual circle area"]) + "cm²", False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(TEXT)
    t.write("Number of sides on the polygon: " + str(n), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(POLYGON)
    t.write("Area of polygon (without using pi): " + str(areaInfo["polygon area"]) + "cm²", False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(TEXT)
    t.write("Pi Estimation: " + str(areaInfo["pi estimate"]), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.write("Pi Estimation Error: " + str(areaInfo["pi error"]), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    
    # Add efficiency metrics display if available
    if "efficiency score" in areaInfo:
        t.write("Efficiency Score: " + str(areaInfo["efficiency score"])[:8], False, align="left", font=("Arial", 12, "bold"))
        t.forward(-spacing)
        t.write("Accuracy per Second: " + str(areaInfo["accuracy per second"])[:8], False, align="left", font=("Arial", 12, "bold"))
        t.forward(-spacing)
    
    t.penup()
    # render center dot
    t.goto(0, 0)
    t.dot(5, DOT)
    rendering = False
    endTime = time.time()
    renderDuration = endTime - startTime
    renderInfo = areaInfo
    for key, value in renderInfo.items():
        try:
            renderInfo[key] = float(value)
        except (TypeError, ValueError):
            pass  # Keep non-numeric values as is
    renderInfo["number of sides"] = n
    renderInfo["render duration"] = renderDuration
    print(renderInfo)


def clickLeft(x, y):
    _n = n
    _n += 1
    init(_n)
    execMain(False)


def clickRight(x, y):
    _n = n
    _n -= 1
    init(_n)
    execMain(False)


def execMain(_init: bool = True, setN = False):
    rendering = False
    t.clear()
    t.goto(0, 0)
    t.penup()
    if _init:
        init(setN)
    drawVizualization()
    screen.onkeypress(execMain, "r")
    screen.onkeypress(exit, "q")
    screen.onkeypress(analyzeAccuracyVsTime, "a")  # Add analysis hotkey
    if not rendering:
        screen.onkeypress(askN, "e")
        screen.onscreenclick(clickLeft, 1)
        screen.onscreenclick(clickRight, 3)


def exit():
    quit()


def analyzeAccuracyVsTime():
    """Run accuracy vs time analysis and display results."""
    try:
        print("\n" + "="*60)
        print("ACCURACY VS TIME ANALYSIS")
        print("="*60)
        
        # Test a range of polygon sides
        test_sides = [3, 6, 12, 24, 50, 100, 200, 500, 1000]
        results = compare_accuracy_vs_time(test_sides, r)
        
        # Find optimal configurations
        optimal_efficiency = find_optimal_trade_off(results, 'efficiency_score')
        optimal_accuracy_per_sec = find_optimal_trade_off(results, 'accuracy_per_second')
        
        print(f"\nRECOMMENDATIONS:")
        print(f"Best overall efficiency: {optimal_efficiency['sides']} sides")
        print(f"  - Pi estimate: {optimal_efficiency['pi_estimate']:.6f}")
        print(f"  - Error: {optimal_efficiency['pi_error']:.6e}")
        print(f"  - Time: {optimal_efficiency['calculation_time']:.6f}s")
        print(f"  - Efficiency score: {optimal_efficiency['efficiency_score']:.2e}")
        
        print(f"\nBest accuracy per second: {optimal_accuracy_per_sec['sides']} sides")
        print(f"  - Accuracy rate: {optimal_accuracy_per_sec['accuracy_per_second']:.2e}")
        
        # Analyze the relationship
        analysis = analyze_accuracy_time_relationship(results)
        if analysis.get('diminishing_returns_point'):
            dim_ret = analysis['diminishing_returns_point']
            print(f"\nDiminishing returns start at: {dim_ret['sides']} sides")
            print("Consider using fewer sides for better efficiency.")
        
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"Analysis not available: {e}")
        print("Make sure pi_analysis.py is available for full functionality.")


def runCommandLineAnalysis():
    """Run analysis in command-line mode without GUI."""
    print("Pi Estimation: Command-Line Analysis Mode")
    print("="*50)
    
    # Initialize variables needed for analysis
    global n, r, angle
    init()  # Initialize default values
    
    # Check if we have command line arguments
    if len(sys.argv) > 1:
        try:
            sides_arg = int(sys.argv[1])
            if sides_arg >= 3:
                n = sides_arg
                r = 150
                angle = 360 / n
                
                # Calculate without GUI
                result = calculate_pi_estimate(n, r)
                efficiency = calculate_efficiency_metrics(result)
                
                print(f"\nResults for {n}-sided polygon:")
                print(f"Pi estimate: {result['pi_estimate']:.8f}")
                print(f"Pi error: {result['pi_error']:.8e}")
                print(f"Accuracy: {result['pi_accuracy']:.6f}")
                print(f"Calculation time: {result['calculation_time']:.6f}s")
                print(f"Efficiency score: {efficiency['efficiency_score']:.2e}")
                return
        except ValueError:
            pass
    
    # Run full analysis
    analyzeAccuracyVsTime()


# Check if running in command-line mode (no GUI available)
if not GUI_AVAILABLE:
    print("GUI not available, running in command-line mode...")
    if ANALYSIS_AVAILABLE:
        runCommandLineAnalysis()
    else:
        print("Analysis module not available. Please ensure pi_analysis.py is present.")
else:
    try:
        execMain(True)
        screen.listen()
        screen.mainloop()
    except Exception as e:
        print(f"GUI initialization failed ({e}), falling back to command-line mode...")
        if ANALYSIS_AVAILABLE:
            runCommandLineAnalysis()
        else:
            print("Analysis module not available. Please ensure pi_analysis.py is present.")
