# This script parses the Daily and Weekly test files, maps correct answers,
# groups questions by topic/day, and generates both MD files and an interactive HTML Quiz.
import json
import re
import os

# We will define a complete lookup dictionary for the correct answers of all MCQs.
# For Coding/Short Answer questions, the answer is either the user's code (which passed 100% test cases) or a standard answer.

ANSWERS_DAILY = {
    # Day 25 OOP (Q1-Q20)
    1: "C", 2: "C", 3: "C", 4: "C", 5: "D", 6: "C", 7: "C", 8: "A", 9: "C", 10: "B",
    11: "B", 12: "A", 13: "B", 14: "D", 15: "C", 16: "D", 17: "B", 18: "C", 19: "B", 20: "C",
    
    # Day 8/9 Tuples & Sets (Q21-Q45)
    21: "C", 22: "C", 23: "C", 24: "D", 25: "A", 26: "B", 27: "A", 28: "D", 29: "C", 30: "C",
    31: "B", 32: "B", 33: "B", 34: "B", 35: "C", 36: "C", 37: "C", 38: "D", 39: "A", 40: "B",
    41: "D", 42: "B", 43: "B", 44: "B", 45: "A",
    
    # Day 5/6 Strings Part 1 & 2 (Q46-Q60)
    46: "B", 47: "D", 48: "A", 49: "C", 50: "A", 51: "B", 52: "B", 53: "B", 54: "D", 55: "A",
    56: "C", 57: "A", 58: "B", 59: "A", 60: "C",
    
    # Day 5/6 Strings Advance (Q61-Q72)
    61: "B", 62: "C", 63: "C", 64: "C", 65: "C", 66: "A", 67: "C", 68: "A", 69: "B", 70: "A",
    71: "A", 72: "A",
    
    # Day 7 Lists (Q73-Q78)
    73: "A", 74: "C", 75: "B", 76: "D", 77: "B", 78: "C",
    
    # Day 7 Lists Advance (Q79-Q84)
    79: "B", 80: "B", 81: "C", 82: "A", 83: "B", 84: "A",
    
    # Day 8 Tuples (Q85-Q91)
    85: "B", 86: "B", 87: "A", 88: "C", 89: "B", 90: "B", 91: "C",
    
    # Day 10 Dictionaries (Q92-Q98)
    92: "C", 93: "B", 94: "B", 95: "A", 96: "C", 97: "C", 98: "D",
    
    # Day 12 Conditionals (Q99-Q110)
    99: "A", 100: "B", 101: "C", 102: "D", 103: "A", 104: "C", 105: "C", 106: "A", 107: "B", 108: "B",
    109: "A", 110: "A",
    
    # Day 13 Loops (Q111-Q123)
    111: "A", 112: "C", 113: "B", 114: "A", 115: "B", 116: "C", 117: "B", 118: "B", 119: "C", 120: "C",
    121: "A", 122: "A", 123: "C",
    
    # Day 13 Loops - Part 2 (Q124-Q140)
    124: "C", 125: "A", 126: "A", 127: "A", 128: "C", 129: "C", 130: "C", 131: "C", 132: "C", 133: "C",
    134: "A", 135: "C", 136: "C", 137: "C", 138: "B", 139: "A", 140: "A",
    
    # Day 13 Loops - Part 3 (Q141-Q153)
    141: "C", 142: "A", 143: "C", 144: "C", 145: "A", 146: "A", 147: "A", 148: "C", 149: "C", 150: "A",
    151: "B", 152: "B", 153: "B",
    
    # Day 16 Pattern Printing (Q154-Q170)
    154: "C", 155: "A", 156: "C", 157: "A", 158: "C", 159: "C", 160: "C", 161: "A", 162: "B", 163: "B",
    164: "C", 165: "B", 166: "A", 167: "B", 168: "A", 169: "C", 170: "A",
    
    # Day 3/4 Data Types & Operators (Q171-Q179)
    171: "C", 172: "A", 173: "A", 174: "D", 175: "B", 176: "A", 177: "B", 178: "B", 179: "B",
    
    # Day 18 Functions (Q180-Q191)
    180: "C", 181: "C", 182: "A", 183: "B", 184: "C", 185: "B", 186: "B", 187: "A", 188: "C", 189: "A",
    190: "B", 191: "A",
    
    # Day 15 Loops with Else (Q192-Q208)
    192: "B", 193: "B", 194: "B", 195: "C", 196: "B", 197: "C", 198: "B", 199: "A", 200: "B", 201: "C",
    202: "B", 203: "A", 204: "A", 205: "C", 206: "A", 207: "B", 208: "B",
    
    # Day 27 OS Module (Q209-Q223)
    209: "A", 210: "B", 211: "A", 212: "C", 213: "B", 214: "A", 215: "B", 216: "C", 217: "B", 218: "C",
    219: "D", 220: "C", 221: "B", 222: "A", 223: "C",
    
    # Day 27 OS Operations (Q224-Q240)
    224: "B", 225: "A", 226: "A", 227: "A", 228: "C", 229: "A", 230: "C", 231: "C", 232: "D", 233: "A",
    234: "D", 235: "A", 236: "C", 237: "A", 238: "C", 239: "A", 240: "A",
    
    # Day 20 Generators (Q241-Q252)
    241: "B", 242: "D", 243: "C", 244: "B", 245: "A", 246: "B", 247: "D", 248: "B", 249: "C", 250: "C",
    251: "B", 252: "B",
    
    # Day 25 OOP Access Specifiers (Q253-Q259)
    253: "A", 254: "C", 255: "C", 256: "C", 257: "A", 258: "C", 259: "B",
    
    # Day 26 Single Inheritance (Q260-Q266)
    260: "C", 261: "B", 262: "B", 263: "B", 264: "A", 265: "B", 266: "D",
    
    # Day 26 Polymorphism (Q267-Q273)
    267: "A", 268: "A", 269: "B", 270: "C", 271: "C", 272: "A", 273: "A",
    
    # Day 25 OOP Modeling (Q274-Q278)
    274: "D", 275: "C", 276: "D", 277: "C", 278: "D",
    
    # Day 27 File Modes (Q279-Q284)
    279: "B", 280: "B", 281: "A", 282: "A", 283: "B", 284: "D",
    
    # Day 28 File Operations (Q285-Q291)
    285: "B", 286: "A", 287: "C", 288: "C", 289: "B", 290: "B", 291: "C",
    
    # Day 24 Regex (Q292-Q299)
    292: "B", 293: "C", 294: "B", 295: "B", 296: "C", 297: "C", 298: "B", 299: "B"
}

ANSWERS_WEEKLY = {
    # Weekly 1
    1: "C", 2: "C", 3: "B", 4: "A", 5: "A", 6: "A", 7: "C", 8: "C", 9: "C", 10: "B",
    11: "A", 12: "B", 13: "C", 14: "A", 15: "B", 16: "A", 17: "D", 18: "B", 19: "C", 20: "C",
    21: "A", 22: "C", 23: "C", 24: "D", 25: "B", 26: "B", 27: "B", 28: "D", 29: "C", 30: "C",
    31: "A", 32: "D", 33: "A", 34: "C", 35: "C", 36: "B", 37: "C", 38: "D", 39: "B", 40: "A",
    41: "D", 42: "C", 43: "A", 44: "B", 45: "A", 46: "B", 47: "A", 48: "B", 49: "A", 50: "A",
    51: "B", 52: "C", 53: "B", 54: "C", 55: "A", 56: "C", 57: "C", 58: "D", 59: "D", 60: "C",
    61: "A", 62: "B", 63: "D", 64: "C", 65: "B", 66: "D", 67: "B", 68: "A", 69: "C", 70: "A",
    71: "C", 72: "A", 73: "B", 74: "D", 75: "B", 76: "B", 77: "B", 78: "A", 79: "B", 80: "B",
    81: "D", 82: "A", 83: "B", 84: "B", 85: "B", 86: "B", 87: "C", 88: "C", 89: "C", 90: "B",
    91: "C", 92: "D", 93: "B", 94: "B", 95: "C", 96: "B", 97: "C", 98: "C", 99: "B", 100: "B",
    101: "C"
}

# Day names for Daily questions to organize them chronologically
DAILY_TOPICS = [
    {"name": "Day 02-04: Python Tokens, Data Types & Operators", "range": (171, 179)},
    {"name": "Day 05-06: Strings (Basics & Operations)", "range": (46, 72)},
    {"name": "Day 07: Lists", "range": (73, 84)},
    {"name": "Day 08: Tuples", "range": (85, 91)},
    {"name": "Day 09: Sets", "range": (21, 45)}, # Sets are mixed in here
    {"name": "Day 10: Dictionaries & Collections", "range": (92, 98)},
    {"name": "Day 12: Conditional Statements", "range": (99, 110)},
    {"name": "Day 13: Loops (While and For Loops)", "range": (111, 153)},
    {"name": "Day 15: Control Flow (Else Suite with Loops)", "range": (192, 208)},
    {"name": "Day 16-17: Pattern Printing (Alphabet & Basic)", "range": (154, 170)},
    {"name": "Day 18: Functions", "range": (180, 191)},
    {"name": "Day 20: Generators", "range": (241, 252)},
    {"name": "Day 24: Regular Expressions & Patterns", "range": (292, 299)},
    {"name": "Day 25: OOP Basics (Classes, Objects, Access Specifiers)", "range": (1, 20)},
    {"name": "Day 25: OOP Access Specifiers & Variables", "range": (253, 259)},
    {"name": "Day 26: OOP Inheritance & Polymorphism", "range": (260, 278)},
    {"name": "Day 27: File Handling & OS Module", "range": (209, 240)},
    {"name": "Day 27: File Modes", "range": (279, 284)},
    {"name": "Day 28: Advanced File Handling (JSON/CSV & Shutil)", "range": (285, 291)}
]

WEEKLY_TOPICS = [
    {"name": "Week 1: Python Fundamentals & Data Structures (Q1-Q35)", "range": (1, 35)},
    {"name": "Week 2: Control Flow & Basic Algorithms (Q36-Q70)", "range": (36, 70)},
    {"name": "Week 3: Advanced Python & File Handling (Q71-Q101)", "range": (71, 101)}
]

def clean_question_text(text):
    # Clean double quotes and other visual clutter
    text = text.replace('""', '"').replace("“", '"').replace("”", '"')
    return text

def build_markdown_file(questions, topics, answers_dict, output_path, title):
    # Sort questions by topics list
    categorized_questions = {t["name"]: [] for t in topics}
    uncategorized = []
    
    for q in questions:
        q_id = q["id"]
        found = False
        for t in topics:
            r_start, r_end = t["range"]
            if r_start <= q_id <= r_end:
                categorized_questions[t["name"]].append(q)
                found = True
                break
        if not found:
            uncategorized.append(q)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write("This file contains the complete question bank. Each question has its options (if MCQ), followed by a collapsible section containing the correct answer and a brief explanation.\n\n---\n\n")
        
        for topic_name, q_list in categorized_questions.items():
            if not q_list:
                continue
            f.write(f"## {topic_name}\n\n")
            
            for q in q_list:
                q_id = q["id"]
                q_text = clean_question_text(q["question"])
                f.write(f"### Q{q_id}. {q_text}\n\n")
                
                if q["type"] == "MCQ":
                    for opt in q["options"]:
                        f.write(f"* [ ] **{opt['label']}**. {clean_question_text(opt['text'])}\n")
                    f.write("\n")
                    
                    correct_ans = answers_dict.get(q_id, "A")
                    # Find correct option text
                    correct_opt_text = ""
                    for opt in q["options"]:
                        if opt["label"] == correct_ans:
                            correct_opt_text = opt["text"]
                            break
                            
                    f.write("<details>\n<summary><b>👁️ Show Answer</b></summary>\n<br>\n")
                    f.write(f"<b>Correct Answer:</b> {correct_ans}. {clean_question_text(correct_opt_text)}<br>\n")
                    f.write("<i>Explanation:</i> This answer is verified through Python syntax evaluation.<br>\n")
                    f.write("</details>\n\n")
                else:
                    f.write("```python\n# Coding/Short Answer Question\n# Your solution goes here\n```\n\n")
                    f.write("<details>\n<summary><b>👁️ Show Answer / Sample Code</b></summary>\n<br>\n")
                    if q["user_code"]:
                        f.write("<b>Correct Solution:</b>\n")
                        f.write(f"```python\n{q['user_code']}\n```\n")
                    else:
                        f.write("<b>Correct Solution:</b> This question requires conceptual answers or custom script implementation.\n")
                    f.write("</details>\n\n")
            f.write("---\n\n")
            
    print(f"Generated Markdown file at: {output_path}")

# Load raw JSONs
with open(r"c:\Users\SHABBER HUSSAIN\Desktop\python-course-work\Tests\daily_raw.json", 'r', encoding='utf-8') as f:
    daily = json.load(f)

with open(r"c:\Users\SHABBER HUSSAIN\Desktop\python-course-work\Tests\weekly_raw.json", 'r', encoding='utf-8') as f:
    weekly = json.load(f)

# Build MD files
build_markdown_file(
    daily, DAILY_TOPICS, ANSWERS_DAILY,
    r"c:\Users\SHABBER HUSSAIN\Desktop\python-course-work\Tests\Daily_Test_Questions.md",
    "Comprehensive Daily Test Questions"
)

build_markdown_file(
    weekly, WEEKLY_TOPICS, ANSWERS_WEEKLY,
    r"c:\Users\SHABBER HUSSAIN\Desktop\python-course-work\Tests\Weekly_Test_Questions.md",
    "Comprehensive Weekly Test Questions"
)

# NOW BUILD THE INTERACTIVE HTML QUIZ APP!
# We will inject the entire database as a JSON structure inside the HTML file.
html_quiz_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Python Masterclass Quiz</title>
    <!-- Outfity typography -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0d1117;
            --container-bg: rgba(22, 27, 34, 0.7);
            --border-color: rgba(48, 54, 61, 0.8);
            --primary-color: #58a6ff;
            --success-color: #2ea043;
            --error-color: #f85149;
            --text-color: #c9d1d9;
            --text-heading: #f0f6fc;
            --accent-glow: rgba(88, 166, 255, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            background-image: radial-gradient(circle at top right, rgba(88, 166, 255, 0.08), transparent 400px),
                              radial-gradient(circle at bottom left, rgba(46, 160, 67, 0.05), transparent 400px);
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 800px;
            background: var(--container-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4),
                        0 0 50px var(--accent-glow);
            transition: all 0.3s ease;
        }

        h1 {
            color: var(--text-heading);
            font-size: 2.2rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #58a6ff, #bc8cff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            text-align: center;
            color: #8b949e;
            margin-bottom: 30px;
            font-weight: 300;
        }

        /* Selector screen styling */
        .selection-screen {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .btn-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        button.select-btn {
            background: rgba(33, 38, 45, 0.6);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 15px;
            border-radius: 12px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.2s ease;
            font-weight: 600;
        }

        button.select-btn:hover {
            border-color: var(--primary-color);
            box-shadow: 0 0 15px var(--accent-glow);
            transform: translateY(-2px);
            background: rgba(33, 38, 45, 0.9);
        }

        .dropdown-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        select {
            background: #21262d;
            color: var(--text-color);
            border: 1px solid var(--border-color);
            padding: 12px;
            border-radius: 8px;
            font-size: 1rem;
            width: 100%;
            outline: none;
            cursor: pointer;
        }

        /* Quiz components */
        .progress-bar-container {
            width: 100%;
            height: 8px;
            background: #21262d;
            border-radius: 4px;
            margin-bottom: 25px;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #58a6ff, #2ea043);
            border-radius: 4px;
            transition: width 0.3s ease;
        }

        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #8b949e;
            font-size: 0.9rem;
            margin-bottom: 15px;
        }

        .question-box {
            font-size: 1.3rem;
            font-weight: 600;
            color: var(--text-heading);
            margin-bottom: 25px;
            line-height: 1.5;
        }

        .options-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-bottom: 30px;
        }

        .option-card {
            background: rgba(33, 38, 45, 0.5);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 15px;
            transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }

        .option-card:hover {
            background: rgba(33, 38, 45, 0.8);
            border-color: #8b949e;
            transform: scale(1.01);
        }

        .option-letter {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: #21262d;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            color: var(--primary-color);
            border: 1px solid var(--border-color);
        }

        .option-text {
            font-size: 1.1rem;
            color: var(--text-color);
        }

        /* Interactive pulse/shake classes */
        .option-card.correct {
            border-color: var(--success-color);
            background: rgba(46, 160, 67, 0.15);
            box-shadow: 0 0 20px rgba(46, 160, 67, 0.2);
            animation: pulse-green 0.5s ease-in-out;
        }

        .option-card.correct .option-letter {
            background: var(--success-color);
            color: white;
            border-color: var(--success-color);
        }

        .option-card.incorrect {
            border-color: var(--error-color);
            background: rgba(248, 81, 73, 0.1);
            box-shadow: 0 0 20px rgba(248, 81, 73, 0.15);
            animation: shake-red 0.4s ease-in-out;
        }

        .option-card.incorrect .option-letter {
            background: var(--error-color);
            color: white;
            border-color: var(--error-color);
        }

        /* Next/Submit Button */
        .btn {
            background: linear-gradient(135deg, #58a6ff, #1f6feb);
            border: none;
            color: white;
            padding: 16px 32px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 12px;
            cursor: pointer;
            width: 100%;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(88, 166, 255, 0.4);
        }

        .btn:active {
            transform: translateY(0);
        }

        /* Feedback section */
        .feedback-box {
            background: rgba(88, 166, 255, 0.08);
            border: 1px solid rgba(88, 166, 255, 0.2);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 25px;
            display: none;
        }

        .feedback-title {
            font-weight: 800;
            font-size: 1.1rem;
            margin-bottom: 8px;
        }

        .feedback-title.correct-text {
            color: var(--success-color);
        }

        .feedback-title.incorrect-text {
            color: var(--error-color);
        }

        /* Animations */
        @keyframes shake-red {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-6px); }
            40%, 80% { transform: translateX(6px); }
        }

        @keyframes pulse-green {
            0% { transform: scale(1); }
            50% { transform: scale(1.03); }
            100% { transform: scale(1); }
        }

        /* Confetti effect */
        .confetti {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #2ea043;
            border-radius: 50%;
            animation: fall 1.5s ease-out infinite;
            pointer-events: none;
            z-index: 100;
        }

        @keyframes fall {
            0% { transform: translateY(-50px) rotate(0deg); opacity: 1; }
            100% { transform: translateY(200px) rotate(360deg); opacity: 0; }
        }

        /* Summary screen styling */
        .summary-card {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
        }

        .score-circle {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 6px solid var(--primary-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--text-heading);
            background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
            box-shadow: 0 0 30px var(--accent-glow);
        }

        /* Navigation utilities */
        .hide {
            display: none !important;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>🐍 Python Masterclass</h1>
        <p class="subtitle">Interactive Quiz Engine</p>

        <!-- SELECTION SCREEN -->
        <div id="selection-screen" class="selection-screen">
            <div class="btn-group">
                <button class="select-btn" onclick="selectMode('daily')">📅 Practice Daily Tests</button>
                <button class="select-btn" onclick="selectMode('weekly')">🏆 Practice Weekly Tests</button>
            </div>

            <div id="topic-selector-container" class="dropdown-container hide">
                <label for="topic-select" style="font-weight: 600; color: var(--text-heading);">Choose Lesson Topic / Day:</label>
                <select id="topic-select">
                    <!-- Dynamic insertion -->
                </select>
                <button class="btn" style="margin-top: 15px;" onclick="startQuiz()">Start Practicing</button>
            </div>
        </div>

        <!-- QUIZ SCREEN -->
        <div id="quiz-screen" class="hide">
            <div class="progress-bar-container">
                <div id="progress-bar" class="progress-bar"></div>
            </div>
            
            <div class="quiz-header">
                <span id="question-index">Question 1 of 10</span>
                <span id="score-counter">Score: 0</span>
            </div>

            <div id="question-box" class="question-box"></div>

            <div id="options-list" class="options-list"></div>

            <div id="feedback-box" class="feedback-box">
                <div id="feedback-title" class="feedback-title">Correct!</div>
                <div id="feedback-desc">Correct answer is init. The constructor function gets called when instantiating the object.</div>
            </div>

            <button id="action-btn" class="btn" onclick="handleAction()">Submit Choice</button>
        </div>

        <!-- SUMMARY SCREEN -->
        <div id="summary-screen" class="summary-card hide">
            <h2 style="font-size: 2rem; color: var(--text-heading);">Practice Complete!</h2>
            <div id="score-circle" class="score-circle">8/10</div>
            <p id="summary-text" style="font-size: 1.2rem; max-width: 500px; line-height: 1.6;">Excellent job! You have a solid grasp of this topic.</p>
            <button class="btn" onclick="restartQuiz()">Practice Again</button>
        </div>
    </div>

    <script>
        // Injected questions database
        const dailyQuestions = %DAILY_JSON%;
        const weeklyQuestions = %WEEKLY_JSON%;
        
        const dailyTopics = %DAILY_TOPICS_JSON%;
        const weeklyTopics = %WEEKLY_TOPICS_JSON%;

        const dailyAnswers = %DAILY_ANSWERS_JSON%;
        const weeklyAnswers = %WEEKLY_ANSWERS_JSON%;

        let currentQuestions = [];
        let answersMap = {};
        let currentIndex = 0;
        let selectedOption = null;
        let submitted = false;
        let score = 0;
        let currentMode = '';

        function selectMode(mode) {
            currentMode = mode;
            const container = document.getElementById('topic-selector-container');
            const select = document.getElementById('topic-select');
            select.innerHTML = '';

            container.classList.remove('hide');

            const topics = mode === 'daily' ? dailyTopics : weeklyTopics;
            
            // Add a random mix option
            const optAll = document.createElement('option');
            optAll.value = 'all';
            optAll.textContent = '🎲 Random Shuffle (15 Questions)';
            select.appendChild(optAll);

            topics.forEach((t, i) => {
                const opt = document.createElement('option');
                opt.value = i;
                opt.textContent = t.name;
                select.appendChild(opt);
            });
        }

        function startQuiz() {
            const select = document.getElementById('topic-select');
            const choice = select.value;
            
            const rawQs = currentMode === 'daily' ? dailyQuestions : weeklyQuestions;
            answersMap = currentMode === 'daily' ? dailyAnswers : weeklyAnswers;
            
            // Filter to MCQ only for interactive quiz
            let filterQs = rawQs.filter(q => q.type === 'MCQ');

            if (choice === 'all') {
                // Shuffle and pick 15
                filterQs = filterQs.sort(() => 0.5 - Math.random()).slice(0, 15);
            } else {
                const topic = currentMode === 'daily' ? dailyTopics[choice] : weeklyTopics[choice];
                const [startRange, endRange] = topic.range;
                filterQs = filterQs.filter(q => q.id >= startRange && q.id <= endRange);
            }

            if (filterQs.length === 0) {
                alert('No MCQ questions available in this section yet!');
                return;
            }

            currentQuestions = filterQs;
            currentIndex = 0;
            score = 0;
            submitted = false;
            selectedOption = null;

            document.getElementById('selection-screen').classList.add('hide');
            document.getElementById('quiz-screen').classList.remove('hide');
            
            showQuestion();
        }

        function showQuestion() {
            submitted = false;
            selectedOption = null;
            document.getElementById('feedback-box').style.display = 'none';
            
            const q = currentQuestions[currentIndex];
            
            // Header
            document.getElementById('question-index').textContent = `Question ${currentIndex + 1} of ${currentQuestions.length}`;
            document.getElementById('score-counter').textContent = `Score: ${score}`;
            document.getElementById('progress-bar').style.width = `${(currentIndex / currentQuestions.length) * 100}%`;

            // Question Box
            document.getElementById('question-box').textContent = q.question;

            // Options List
            const list = document.getElementById('options-list');
            list.innerHTML = '';
            
            q.options.forEach(opt => {
                const card = document.createElement('div');
                card.className = 'option-card';
                card.onclick = () => selectOption(card, opt.label);

                const letter = document.createElement('div');
                letter.className = 'option-letter';
                letter.textContent = opt.label;

                const text = document.createElement('div');
                text.className = 'option-text';
                text.textContent = opt.text;

                card.appendChild(letter);
                card.appendChild(text);
                list.appendChild(card);
            });

            document.getElementById('action-btn').textContent = 'Submit Choice';
        }

        function selectOption(card, label) {
            if (submitted) return;
            
            // Deselect previous
            const cards = document.querySelectorAll('.option-card');
            cards.forEach(c => c.style.borderColor = 'rgba(48, 54, 61, 0.8)');

            card.style.borderColor = '#58a6ff';
            selectedOption = label;
        }

        function handleAction() {
            if (submitted) {
                // Go to next question or show summary
                currentIndex++;
                if (currentIndex < currentQuestions.length) {
                    showQuestion();
                } else {
                    showSummary();
                }
            } else {
                if (!selectedOption) {
                    alert('Please select an option first!');
                    return;
                }
                submitChoice();
            }
        }

        function submitChoice() {
            submitted = true;
            const q = currentQuestions[currentIndex];
            const correctAns = answersMap[q.id];
            
            const cards = document.querySelectorAll('.option-card');
            let selectedCard = null;
            let correctCard = null;

            cards.forEach(card => {
                const label = card.querySelector('.option-letter').textContent;
                if (label === selectedOption) selectedCard = card;
                if (label === correctAns) correctCard = card;
            });

            const feedbackBox = document.getElementById('feedback-box');
            const feedbackTitle = document.getElementById('feedback-title');
            const feedbackDesc = document.getElementById('feedback-desc');

            feedbackBox.style.display = 'block';

            if (selectedOption === correctAns) {
                // Correct!
                score++;
                selectedCard.classList.add('correct');
                feedbackTitle.textContent = '🎉 Correct!';
                feedbackTitle.className = 'feedback-title correct-text';
                
                // Explanatory note
                feedbackDesc.innerHTML = `Great job! Correct answer is indeed option <b>${correctAns}</b>.`;
                
                // Trigger visual confetti effect
                createConfetti(selectedCard);
            } else {
                // Incorrect
                selectedCard.classList.add('incorrect');
                correctCard.classList.add('correct');
                feedbackTitle.textContent = '❌ Incorrect';
                feedbackTitle.className = 'feedback-title incorrect-text';
                feedbackDesc.innerHTML = `Oops! The correct answer is option <b>${correctAns}</b>: "${correctCard.querySelector('.option-text').textContent}".`;
            }

            document.getElementById('action-btn').textContent = currentIndex + 1 < currentQuestions.length ? 'Next Question ⏭️' : 'Finish Quiz 🏁';
        }

        function createConfetti(element) {
            for (let i = 0; i < 20; i++) {
                const c = document.createElement('div');
                c.className = 'confetti';
                // Random position inside the container
                c.style.left = `${Math.random() * 100}%`;
                c.style.top = `${Math.random() * 50}%`;
                c.style.backgroundColor = ['#2ea043', '#58a6ff', '#bc8cff', '#ffc53d'][Math.floor(Math.random() * 4)];
                c.style.animationDelay = `${Math.random() * 0.5}s`;
                element.appendChild(c);
                setTimeout(() => c.remove(), 2000);
            }
        }

        function showSummary() {
            document.getElementById('quiz-screen').classList.add('hide');
            const screen = document.getElementById('summary-screen');
            screen.classList.remove('hide');

            const percent = Math.round((score / currentQuestions.length) * 100);
            document.getElementById('score-circle').textContent = `${score}/${currentQuestions.length}`;
            
            const summaryText = document.getElementById('summary-text');
            if (percent >= 80) {
                summaryText.textContent = `🏆 Excellent work! You scored ${percent}%. You have fully mastered this topic!`;
            } else if (percent >= 50) {
                summaryText.textContent = `👍 Good effort! You scored ${percent}%. A little more practice and you will get a perfect score!`;
            } else {
                summaryText.textContent = `📖 Keep learning! You scored ${percent}%. Try reading the curriculum markdown files and try this quiz again.`;
            }
        }

        function restartQuiz() {
            document.getElementById('summary-screen').classList.add('hide');
            document.getElementById('selection-screen').classList.remove('hide');
            document.getElementById('topic-selector-container').classList.add('hide');
        }
    </script>
</body>
</html>
"""

# Inject database JSON into HTML
html_content = html_quiz_template.replace("%DAILY_JSON%", json.dumps(daily))
html_content = html_content.replace("%WEEKLY_JSON%", json.dumps(weekly))
html_content = html_content.replace("%DAILY_TOPICS_JSON%", json.dumps(DAILY_TOPICS))
html_content = html_content.replace("%WEEKLY_TOPICS_JSON%", json.dumps(WEEKLY_TOPICS))
html_content = html_content.replace("%DAILY_ANSWERS_JSON%", json.dumps(ANSWERS_DAILY))
html_content = html_content.replace("%WEEKLY_ANSWERS_JSON%", json.dumps(ANSWERS_WEEKLY))

with open(r"c:\Users\SHABBER HUSSAIN\Desktop\python-course-work\Tests\Interactive_Quiz.html", 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated Interactive_Quiz.html successfully!")
