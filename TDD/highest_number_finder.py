class HighestNumberFinder:

    def find_highest_number(self, numbers):
        result =numbers[0]
        if len(numbers) > 1:
            if numbers[1] > result:
                result = numbers[1]

        return result