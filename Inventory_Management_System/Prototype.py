# This class is used to create widgets and add them to bins
# Then export those bins into files that are to be ran through wsms
class WidgetBin:

    def __init__(self):
        self.bins = {}

    # This Creates the bin for the widgets and updates that bin with a widget.
    def add_widgets_to_bin(self, name, quantity):
        # todo: Check to see if the widget is already in the list then add the new value to the existing value
        #  instead of replacing
        widget = {name: quantity}
        self.bins.update(widget)

    # Taking the user input and adding the widget to a bin
    def widget_to_bin_request(self):
        widget_name = str(input("Please enter the widget name: "))
        widget_quantity = int(input("Please enter the quantity for that widget: "))
        self.add_widgets_to_bin(widget_name, widget_quantity)

    def widget_bin_export(self, total):
        # todo: Add try catch for if the file already exists
        file_name = str(input("Please enter the name for this bin: "))
        bin_file = open(file_name + ".txt", 'x')
        # Adds Widgets to each line of the file
        for key in self.bins:
            bin_file.write(key + ': ' + str(self.bins[key]))
            bin_file.write("\n")
        print("Number of widgets added to this bin: " + total)
        bin_file.close()

    # Checking to see if the user wants to enter another widget.
    def widget_bin_completion(self):
        keep_going = True
        total_widgets = 0
        self.widget_to_bin_request()
        while keep_going is not False:
            user_input = input("Would you like to enter another widget?(Enter 1 for Yes or 2 for No): ")
            # If the user is finished or the bin has reach maximum capacity then the bin will be converted into a file.
            # The widgets will then be put on each line as they were entered with the name and quantity.
            # todo: Need to add message statement saying you have reach capacity
            # todo: Need to add a catch for if the bin goes over 1000
            values = self.bins.values()
            total_widgets = sum(values)
            if user_input != "1" or total_widgets == 1000:
                keep_going = False
                self.widget_bin_export(total_widgets)
            # If the user wishes to continue entering widgets
            else:
                self.widget_to_bin_request()
