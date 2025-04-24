import speech_recognition as sr
from ..utils.logger import logger

class SpeechService:
    """Handles speech recognition functionality"""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphones = self.get_microphone_list()
        self.mic_index = 0 if not self.microphones else self.microphones[0][1]
        logger.info(f"Speech service initialized with microphone index {self.mic_index}")


    def get_microphone_list(self):
        """Get list of available microphones that start with 'Microphone'"""
        try:
            mic_names = sr.Microphone.list_microphone_names()
            # Create list of tuples with (mic_name, index) only for mics starting with "Microphone"
            filtered_mics = [
                (name, idx) for idx, name in enumerate(mic_names) 
                if name.startswith("Microphone")
            ]
            
            if not filtered_mics:
                logger.warning("No microphones found starting with 'Microphone', using default")
                return [("Default Microphone", 0)]
                
            logger.info(f"Found {len(filtered_mics)} compatible microphones")
            return filtered_mics
            
        except Exception as e:
            logger.error(f"Failed to get microphone list: {str(e)}")
            return [("Default Microphone", 0)]
        
    def set_microphone(self, index):
        """Set the active microphone by index"""
        self.mic_index = index
        logger.debug(f"Microphone index set to {index}")

    def listen(self, callback):
        """
        Start listening for speech and convert to text
        Args:
            callback: Function to call with status updates
        """
        try:
            with sr.Microphone(device_index=self.mic_index) as source:
                logger.debug("Adjusting for ambient noise...")
                callback("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                logger.info("Listening...")
                callback("Listening...")
                audio = self.recognizer.listen(source, timeout=5)
                
                logger.debug("Processing speech...")
                callback("Processing speech...")
                text = self.recognizer.recognize_google(audio)
                
                logger.info(f"Recognized: {text}")
                callback(f"You said: {text}")
                return text

        except sr.WaitTimeoutError:
            message = "No speech detected"
            logger.warning(message)
            callback(message)
        except sr.UnknownValueError:
            message = "Could not understand audio"
            logger.warning(message)
            callback(message)
        except sr.RequestError as e:
            message = f"Could not request results: {str(e)}"
            logger.error(message)
            callback(message)
        except Exception as e:
            message = f"Error: {str(e)}"
            logger.error(message)
            callback(message)
        return None