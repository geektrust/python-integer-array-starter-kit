class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses each input and assigns it *
        * to different variables.                      *
        ***********************************************

        Format of input_str: "[2, 7, 11, 15]"

        Your final output needs to be printed to the console.
        """

       # Remove brackets if present
        cleaned = input_str.strip().strip("[]")

        # Convert to integers
        arr = [int(x.strip()) for x in cleaned.split(",") if x.strip()]

        # Output
        print("Array:", arr)
