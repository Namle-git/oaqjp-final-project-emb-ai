"""
This is a module docsting
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emtote_detect():
    """
    This is a docstring
    """
    # Retrieve text
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to function
    response = emotion_detector(text_to_analyze)
    # Add condition to enter text
    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!"
    # Return a formatted string
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
           f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
           f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
           f"The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """
    This is a docstring
    """
    # Render the text
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
