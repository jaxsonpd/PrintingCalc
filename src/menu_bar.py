## @file MenuBar.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-04-20
#  @brief The file contains the menubar for the main calculator window

import tkinter as tk


class MenuBar:
    """
    Menu bar class which contains the formatting and functionality 
    for the main menu
    """
    def __init__(self, master: tk.Widget) -> None:
        """
        Initialise the class

        @param master the master widget to make this a child of
        """
        self.master = master
        self.menu = tk.Menu(self.master)

        self.filemenu = self.__create_filemenu()

        # Add menus to the menu bar
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.master.config(menu=self.menu)

    def __create_filemenu(self) -> None:
        """ Create the file menu """
        filemenu = tk.Menu(self.menu, tearoff=0)

        filemenu.add_command(label="New Window")
        filemenu.add_separator()

        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as")
        filemenu.add_separator()
        
        filemenu.add_command(label="Preferences")
        filemenu.add_separator()
        
        filemenu.add_command(label="Clear")
        filemenu.add_command(label="Exit", command=self.master.quit)

        return filemenu