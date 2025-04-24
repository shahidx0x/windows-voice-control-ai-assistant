import tkinter as tk
import threading
from .components import LogArea, CommandButton, MicrophoneSelector
from ..services.speech_service import SpeechService
from ..utils.logger import logger
from ..constants.strings import AppStrings

class MainWindow:
    """Main application window"""
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        
        # Initialize services
        self.speech_service = SpeechService()
        
        # Initialize UI components
        self.setup_components()
        
        logger.info(AppStrings.APP_INIT)

    def setup_window(self):
        """Configure the main window properties"""
        self.root.title(AppStrings.WINDOW_TITLE)
        self.root.geometry(AppStrings.WINDOW_GEOMETRY)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=AppStrings.WINDOW_BG_COLOR)
        
        # Add window close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_components(self):
        """Initialize and configure UI components"""
        # Create microphone selector
        mic_list = self.speech_service.get_microphone_list()
        self.mic_selector = MicrophoneSelector(
            self.root,
            mic_list,
            self.on_mic_select
        )

        # Create command button
        self.command_button = CommandButton(
            self.root,
            self.on_button_click
        )

        # Create log area
        self.log_area = LogArea(self.root)
        self.log_area.log(AppStrings.APP_STARTED)

    def on_mic_select(self, event):
        """Handle microphone selection"""
        selected_mic = event.widget.get()
        # Get the actual device index instead of the combobox index
        mic_index = self.mic_selector.get_selected_index()
        self.speech_service.set_microphone(mic_index)
        self.log_area.log(AppStrings.MIC_CHANGED.format(selected_mic))
        logger.info(AppStrings.MIC_CHANGED.format(selected_mic))

    def on_button_click(self):
        """Handle command button click"""
        threading.Thread(
            target=self.start_listening,
            daemon=True
        ).start()

    def start_listening(self):
        """Start speech recognition in a separate thread"""
        self.speech_service.listen(self.log_area.log)

    def on_closing(self):
        """Handle window closing"""
        logger.info(AppStrings.APP_SHUTDOWN)
        self.root.destroy()

    def run(self):
        """Start the application main loop"""
        try:
            self.root.mainloop()
        except Exception as e:
            logger.error(AppStrings.APP_ERROR.format(str(e)))
            raise