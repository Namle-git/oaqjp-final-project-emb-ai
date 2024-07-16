from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_analyzer(self):
        # Test joy emotion
        emotion1 = emotion_detector('I am glad this happened')
        self.assertEqual(emotion1['dominant_emotion'], 'joy')

        # Test anger emotion
        emotion2 = emotion_detector('I am really mad about this')
        self.assertEqual(emotion2['dominant_emotion'], 'anger')

        # Test disgust emotion
        emotion3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(emotion3['dominant_emotion'], 'disgust')

        # Test sadness emotion
        emotion4 = emotion_detector('I am so sad about this')
        self.assertEqual(emotion4['dominant_emotion'], 'sadness')

        # Test fear emotion
        emotion5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(emotion5['dominant_emotion'], 'fear')

unittest.main()