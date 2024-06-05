## @file MenuBar.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-04-20
#  @brief The file contains the menubar for the main calculator window

import tkinter as tk

from copy import copy

class MenuBar(tk.Menu):
    """
    Menu bar class which contains the formatting and functionality 
    for the main menu
    """
    def __init__(self, master: tk.Widget, histories : list) -> None:
        """
        Initialise the class

        ### Params:
        master : tk.Widget
         The master widget to make this a child of
        histories : list
         A list of the current histories

        ### Variables:
        histories : list
         A list of history objects that are currently in use in the application
        """
        super().__init__(master)
        self.master = master

        ## The histories that are currently in use in the application
        self.histories = histories

        self.filemenu = self.__create_filemenu()

        # Add menus to the menu bar
        self.add_cascade(label="File", menu=self.filemenu)

        self.master.config(menu=self)

    def __create_filemenu(self) -> None:
        """ Create the file menu """
        filemenu = tk.Menu(self, tearoff=0)

        filemenu.add_command(label="New Window")
        filemenu.add_separator()

        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as")
        filemenu.add_separator()
        
        filemenu.add_command(label="Preferences")
        filemenu.add_separator()
        
        filemenu.add_command(label="Clear", command=self.__clear_history)
        filemenu.add_command(label="Exit", command=self.master.quit)

        return filemenu

    def __clear_history(self, event : tk.Event = None):
        """
        Clear the current history called by the file->clear option

        ### Params:
        event : tk.Event
         The event object
        """

        ## Find the active history and clear it 
        for history in self.histories:
            if (bool(history.grid_info())):
                for equation in copy(history.equations):
                    equation.delete_equation()

                self.master.update_idletasks()
                history.scroll("top")
                history.test_update()
                self.master.grid_propagate(0)
                print(history.inner.winfo_height())

                break