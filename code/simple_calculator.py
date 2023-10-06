# class SimpleCalculator:
#     def __init__(self):
#         #Instantiate any data attributes
#         self.operand1 = None
#         self.operand2 = None
#         self.oper = None
#         self.hist = []
#         self.ans = None

#     def evaluate_expression(self, inp):
#         """
#         Evaluate the input expression and return the output as a float
#         Return a string "Error" if the expression is invalid
#         """
#         self.inp = inp.strip().split()
#         self.ans = None
#         if len(self.inp) == 3:
#             try:
#                 self.operand1 = int(self.inp[0])
#                 self.operand2 = int(self.inp[2])
#                 self.oper = self.inp[1]
#                 if self.oper == "+":
#                     self.ans = float(self.operand1 + self.operand2)
#                 elif self.oper == "-":
#                     self.ans = float(self.operand1 - self.operand2)
#                 elif self.oper == "*":
#                     self.ans = float(self.operand1*self.operand2)
#                 elif self.oper == "/":
#                     self.ans = float(self.operand1/self.operand2)
#                 else:
#                     self.ans = "Error"
#             except:
#                 self.ans = "Error"
#         else:
#             self.ans =  "Error"
#         self.hist.insert(0,(inp,self.ans))
#         return self.ans

#     def get_history(self):
#         """
#         Return history of expressions evaluated as a list of (expression, output) tuples
#         The order is such that the most recently evaluated expression appears first 
#         """
#         return self.hist

class SimpleCalculator:
    def __init__(self):
        #Instantiate any data attributes
        self.operand1 = None
        self.operand2 = None
        self.oper = None
        self.hist = []
        self.ans = None

    def evaluate_expression(self, inp):
        """
        Evaluate the input expression and return the output as a float
        Return a string "Error" if the expression is invalid
        """
        self.inp = inp.strip()
        if len(self.inp)<3:
            self.ans = "Error"
        else:
            i = 1
            self.operand1 = self.inp[0]
            while (i < len(self.inp)) and (self.inp[i] not in ["+","-","/","*"]):
                self.operand1 += self.inp[i]
                i += 1
            if i == len(self.inp):
                return "Error"
            self.oper = self.inp[i]
            self.operand2 = self.inp[i+1:]
            if self.operand1 != "" and self.oper != "" and self.operand2 != "":
                try:
                    self.operand1 = int(self.operand1.strip())
                    if self.oper == "-" and self.operand2.strip()[0] == "+":
                        self.ans = "Error"
                    self.operand2 = int(self.operand2.strip())
                    if self.oper == "+":
                        if self.operand2 < 0:
                            self.ans = "Error"
                        else:
                            self.ans = float(self.operand1 + self.operand2)
                    elif self.oper == "-" and self.ans != "Error":
                        self.ans = float(self.operand1 - self.operand2)
                    elif self.oper == "*":
                        self.ans = float(self.operand1*self.operand2)
                    elif self.oper == "/":
                        self.ans = float(self.operand1/self.operand2)
                    else:
                        self.ans = "Error"
                except:
                    self.ans = "Error"
            else:
                self.ans =  "Error"
            self.hist.insert(0,(inp,self.ans))
        return self.ans

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples
        The order is such that the most recently evaluated expression appears first 
        """
        return self.hist
# inst = SimpleCalculator()
# print(inst.evaluate_expression(" <write your expression here> "))