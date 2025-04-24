import tkinter as tk
from tkinter import scrolledtext, ttk
import tkinter.font as tkfont
from ..constants.components import UIConstants

class LogArea:
    """A scrollable text area for logging messages"""
    def __init__(self, root):
        self.text_widget = scrolledtext.ScrolledText(
            root, 
            width=50, 
            height=20, 
            wrap=tk.WORD, 
            fg=UIConstants.LIGHT_TEXT, 
            bg=UIConstants.LOG_BG, 
            font=(UIConstants.FONT_COURIER, UIConstants.SIZE_SMALL)
        )
        self.text_widget.pack(padx=10, pady=10)
        self.text_widget.config(state=tk.DISABLED)

    def log(self, message):
        """Add a message to the log area"""
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, message + '\n')
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.yview(tk.END)

class CommandButton:
    """A button that triggers speech recognition"""
    def __init__(self, root, command):
        self.button = tk.Button(
            root, 
            text=UIConstants.BUTTON_TEXT, 
            command=command,
            fg=UIConstants.LIGHT_TEXT, 
            bg=UIConstants.BUTTON_BG, 
            font=(UIConstants.FONT_ARIAL, UIConstants.SIZE_MEDIUM)
        )
        self.button.pack()

class MicrophoneSelector:
    """A Material Design dropdown for selecting the input microphone"""
    def __init__(self, root, mic_list, on_select):
        self.mic_names = [mic[0] for mic in mic_list]
        self.mic_indices = [mic[1] for mic in mic_list]

        # Create style for material design look
        style = ttk.Style()
        style.configure(
            UIConstants.COMBOBOX_STYLE,
            background=UIConstants.DARKER_BG,
            fieldbackground=UIConstants.DARKER_BG,
            foreground=UIConstants.LIGHT_TEXT,
            arrowcolor=UIConstants.LIGHT_TEXT,
            selectbackground=UIConstants.SELECT_BG,
            selectforeground=UIConstants.LIGHT_TEXT
        )

        # Container frame
        self.frame = tk.Frame(root, bg=UIConstants.DARK_BG)
        self.frame.pack(fill=tk.X, padx=20, pady=(15,5))

        # Label with material design font
        label_font = tkfont.Font(
            family=UIConstants.FONT_SEGOE, 
            size=UIConstants.SIZE_SMALL, 
            weight="normal"
        )
        self.label = tk.Label(
            self.frame, 
            text=UIConstants.MIC_SELECT_TEXT, 
            fg=UIConstants.ACCENT_BLUE,
            bg=UIConstants.DARK_BG, 
            font=label_font
        )
        self.label.pack(anchor="w", pady=(0,5))

        # Combobox container for full width effect
        self.combo_frame = tk.Frame(self.frame, bg=UIConstants.DARK_BG)
        self.combo_frame.pack(fill=tk.X)
        
        # Configure grid for full width
        self.combo_frame.grid_columnconfigure(0, weight=1)

        # Combobox with material design style
        self.combo = ttk.Combobox(
            self.combo_frame,
            values=self.mic_names,
            state="readonly",
            style=UIConstants.COMBOBOX_STYLE
        )
        self.combo.grid(row=0, column=0, sticky="ew")
        
        # Set default selection
        if self.mic_names:
            self.combo.current(0)  # Set first item as selected
        else:
            self.combo.set(UIConstants.NO_MIC_TEXT)
            
        # Bind selection event
        self.combo.bind('<<ComboboxSelected>>', on_select)
        
        # Trigger selection event for default value
        if self.mic_names:
            self.combo.event_generate('<<ComboboxSelected>>')

        # Add bottom border effect
        self.border = tk.Frame(
            self.frame, 
            height=2, 
            bg=UIConstants.ACCENT_BLUE
        )
        self.border.pack(fill=tk.X, pady=(0,5))