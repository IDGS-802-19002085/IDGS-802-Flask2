class Operaciones:

    numeros = []

    def __init__(self, nums):
        self.numeros.clear()
        for num in nums:
            self.numeros.append(int(nums.get(num)))

    def nums(self):
        return self.numeros

    def maximo(self):
        return max(self.numeros)
    def minimo(self):
        return min(self.numeros)
    def promedio(self):
        return sum(self.numeros) / len(self.numeros)
    def masRep(self):
        contador = {}
        for num in self.numeros:
            if num in contador:
                contador[num] += 1
            else:
                contador[num] = 1
        masReps = {}
        for reps in contador:
            if contador[reps] > 1:
                masReps[reps] = contador[reps]
        return masReps