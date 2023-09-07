class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def evaluate_at(self, x):
        result = 0
        for i in range(len(self.coeffs)):
            result += self.coeffs[i] * x**(len(self.coeffs)-1-i)
        return result

    def __add__(self, other):
        # 创建新列表存储结果
        result_coeffs = [] 
        max_degree = max(len(self.coeffs), len(other.coeffs)) - 1
        for i in range(max_degree+1):
            result_coeffs.append(0) 

        # 依次添加系数
        for i in range(len(self.coeffs)):
            result_coeffs[i] += self.coeffs[i]
        for i in range(len(other.coeffs)):
            result_coeffs[max_degree-i] += other.coeffs[i]

        return Polynomial(result_coeffs)

    def __iadd__(self, other):
        new_poly = self.__add__(other)
        self.coeffs = new_poly.coeffs
        return self

    def __str__(self):
        result = ""
        for i in range(len(self.coeffs)):
            term = ""
            if self.coeffs[i] != 0:
                if i == 0:
                    term += str(self.coeffs[i])
                else:
                    term += str(self.coeffs[i]) + "x^" + str(len(self.coeffs)-i-1)
            
            if i > 0:
                term += " + "
            result += term
        return result[:-3]


def main():
    # 1x^4 + 2x^3 + 3x^2 + 4x + 5
    coeffs = [1,2,3,4,5]
    poly = Polynomial(coeffs)
    print(poly.evaluate_at(2))   # 57
    print(poly.evaluate_at(3))   # 179
    print(poly)  # Outputs: 1x^4 + 2x^3 + 3x^2 + 4x^1 + 5

    # 4x^3 + 6x^2 + 8x^1 + 10
    coeffs = [4,6,8,10]
    poly2 = Polynomial(coeffs)
    print(poly2)  # Outputs: 4x^3 + 6x^2 + 8x^1 + 10
    poly += poly2
    print(poly)  # Outputs: 1x^4 + 6x^3 + 9x^2 + 12x^1 + 15

if __name__ == '__main__':
    main()
