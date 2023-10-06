from stack import Stack
from simple_calculator import SimpleCalculator

class AdvancedCalculator(SimpleCalculator):
    def __init__(self):
        """
        Call super().__init__()
        Instantiate any additional data attributes
        """
        SimpleCalculator.__init__(self)
        self.tokens = []
        self.count_open1 = 0
        self.count_close1 = 0
        self.count_open2 = 0
        self.count_close2 = 0
        self.count_open3 = 0
        self.count_close3 = 0

    def tokenize(self, input_expression):
        """
        Convert the input string expression to tokens and return this list.
        Each token is either an integer operand or a character operator or bracket.
        """
        self.inp = input_expression
        temp = self.inp.strip()
        temp = temp.split()
        x = []
        for i in range(len(temp)):
            num=""
            for j in range(len(temp[i])):
                if num!="" and temp[i][j] in ["+","-","/","*","(","{","[",")","}","]"]:
                    x.append(int(num))
                    num =""
                    x.append(temp[i][j])
                elif temp[i][j] in ["(","{","[",")","}","]","+","-","/","*"]:
                    x.append(temp[i][j])
                elif ord(temp[i][j])>=48 and ord(temp[i][j])<=57:
                    num += temp[i][j]
                else:
                    self.ans = "Error"
                    break
            if num != "":
                if num in ["+","-","/","*"]:
                    x.append(num)
                else:
                    x.append(int(num))
        return x            

    def check_brackets(self, list_tokens):
        """
        Check if brackets are valid, that is, all open brackets are closed by the same type 
        of brackets. Also, () contains only () brackets.
        Return True if brackets are valid, False otherwise.
        """
        hi = 0
        print(self.tokens)        ###
        while hi < len(list_tokens):
            if self.ans == "Error":
                break
            if list_tokens[hi] == "{":
                self.count_open1 += 1
            elif list_tokens[hi] == "}":
                self.count_close1 += 1
            elif list_tokens[hi] == "(":
                self.count_open2 += 1
                hi += 1
                while self.count_open2 != self.count_close2 and hi < len(list_tokens):
                    if list_tokens[hi] in ["{","}"]:
                        self.ans = "Error"
                        break
                    elif list_tokens[hi] == ")":
                        self.count_close2 += 1
                    elif list_tokens[hi] == "(":
                        self.count_open2 += 1
                    hi += 1
                else:
                    if hi >= len(list_tokens):
                        break
                    else:
                        hi -= 1
            elif type(list_tokens[hi]) != int and list_tokens[hi] not in ["+","-","*","/"]:
                self.ans = "Error"
                break
            hi += 1
        if self.ans == "Error" or self.count_open1 != self.count_close1:
            return False
        else:
            return True

    def check(self,list_tokens):
        print(list_tokens)           ###
        if list_tokens[-1] in ["+","-","*","/"]:
            self.ans = "Error"
            return False
        if "+" not in list_tokens and "*" not in list_tokens and "/" not in list_tokens and "-" not in list_tokens:
            self.ans = "Error"
            return False
        return True
        
    def evaluate_list_tokens(self, list_tokens):
        """
        Evaluate the expression passed as a list of tokens.
        Return the final answer as a float, and "Error" in case of division by zero and other errors.
        """
        # Evaluating by converting to postfix expression
        def evaluate(a,b,oper):
            try:
                self.operand1 = a
                self.operand2 = b
                self.oper = oper
                if self.oper == "+":
                    return float(self.operand1 + self.operand2)
                elif self.oper == "-":
                    return float(self.operand1 - self.operand2)
                elif self.oper == "*":
                    return float(self.operand1*self.operand2)
                elif self.oper == "/":
                    return float(self.operand1/self.operand2)
                else:
                    return "Error"
            except:
                return "Error"
        def check_priority(oper1,oper2):
            order = ["/","*","-","+"]
            if order.index(oper1) < order.index(oper2):
                return True
            else:
                return False
        # infix to postfix
        print(self.tokens)            ###
        aux = Stack()
        expression = Stack()
        for i in range(len(self.tokens)):
            if self.tokens[i] == '(' or self.tokens[i] == "{" or self.tokens[i] == "[":
                aux.push(self.tokens[i])
            elif type(self.tokens[i]) == int:
                expression.push(self.tokens[i])
            elif self.tokens[i] in ["/","*","+","-"]:
                if aux.peek() in ["/","*","+","-"]:
                    if check_priority(self.tokens[i],aux.peek()):
                        aux.push(self.tokens[i])
                    else:
                        while aux.is_empty() == False and (check_priority(self.tokens[i],aux.peek())) == False:
                            temp = aux.peek()
                            aux.pop()
                            expression.push(temp)
                            temp = aux.peek()
                            if temp == "(" or temp == "{" or temp == "[":
                                break
                        aux.push(self.tokens[i])
                else:
                    aux.push(self.tokens[i])
            else:
                f = 0
                print(aux)          ### 
                if self.tokens[i] == ")":
                    f = 1
                    while aux.peek() != "(":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "}":
                    f = 1
                    while aux.peek() != "{":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "]":
                    f = 1
                    while aux.peek() != "[":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                if f==1:
                    aux.pop()
        print(aux)                   ###
        while aux.is_empty() == False:
            temp = aux.peek()
            aux.pop()
            expression.push(temp)
        print(expression)             ###
        # Evaluating the postfix expression
        try:
            spare = Stack()
            exp = Stack()
            for i in range(len(expression)):
                z = expression.peek()
                expression.pop()
                exp.push(z)
            print(exp)               ###
#postfix to infix correct!
#solving the postfix expression
            i = 0
            while exp.is_empty() == False:
                while exp.peek() not in ["+","-","/","*"]:
                    y = exp.peek()
                    exp.pop()
                    spare.push(y)
                b = spare.peek()
                spare.pop()
                a = spare.peek()
                spare.pop()
                op = exp.peek()
                exp.pop()
                spare.push(evaluate(a,b,op))
            self.ans = spare.peek()
            spare.pop()
            if spare.is_empty() == False:
                self.ans = "Error"
        except:
            self.ans = "Error"
        return self.ans
            
    def evaluate_expression(self, input_expression):
        """
        Evaluate the input expression and return the output as a float.
        Return a string "Error" if the expression is invalid.
        """
        self.tokens = self.tokenize(input_expression)
        print(self.tokens)          ###
        if self.check_brackets(self.tokens) and self.check(self.tokens):
            self.ans = self.evaluate_list_tokens(self.tokens)
        else:
            print("hi")             ###
            self.ans = "Error"
        self.hist.insert(0, (self.inp, self.ans))
        return self.ans

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples.
        The order is such that the most recently evaluated expression appears first.
        """
        return self.hist
    
inst = AdvancedCalculator()
# print(inst.check_brackets(inst.tokenize(" ()  8+++++!{}(){}()")))
print(inst.evaluate_expression("{2 + (3 * 4) / (5 - 1)} * 3 + 2 - 1 + {4 * (5 - 2)} * 0 + 1"))



# 2 + 3 * (4 - 1)