class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # There are cars going in the same direction on one lane highway
        # Given two array, one for position of each car and speed for each car in mph

        #Constraints
            # A car cant pass another car, it can only catch up, and drive at the same speed.
            # Car fleet: Non empty set of cars driving at the same position and speed.
                # A single car counts
            # Has to reach the destination together


            cars = list(zip(position, speed))
            cars.sort(reverse = True)

            stack = []

            for p, s in cars:
                time = (target - p) / s
                if not stack or time > stack[-1]:
                    stack.append(time)
            return len(stack)



        