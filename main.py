class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses each input and assigns it *
        * to different variables.                      *
        ***********************************************

        Format of input_str: "2, 7, 11, 15"

        Your final output needs to be printed to the console.
        """

        # Parse array and integer
        arr = [int(x.strip()) for x in input_str.split(",")]

        # Output
        print("Array:", arr)
