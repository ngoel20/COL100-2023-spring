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
                if num!="" and temp[i][j] in ["+","-","/","*"]:
                    x.append(int(num))
                    num =""
                    x.append(temp[i][j])
                elif temp[i][j] in ["(","{","[",")","}","]"]:
                    x.append(temp[i][j])
                else:
                    num += temp[i][j]
            if num != "":
                x.append(int(num))
        return x            

    def check_brackets(self, list_tokens):
        """
        Check if brackets are valid, that is, all open brackets are closed by the same type 
        of brackets. Also, () contains only () brackets.
        Return True if brackets are valid, False otherwise.
        """
        i = 0
        while i < len(self.tokens):
            if self.tokens[i] == "{":
                self.count_open1 += 1
            if self.tokens[i] == "(":
                self.count_open2 += 1
                while self.count_open2 != self.count_close2 and i < len(self.tokens):
                    if self.tokens[i] == "{":
                        self.ans = "Error"
                    i += 1
            if i >= len(self.tokens):
                if self.count_open1 != self.count_close1:
                    self.ans = "Error"
                break
            i += 1
        if self.ans == "Error":
            return False
        else:
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
            order = ["/","*","+","-"]
            if order.index(oper1) < order.index(oper2):
                return True
            else:
                return False
        # infix to postfix 
        aux = Stack()
        expression = Stack()
        for i in range(len(self.tokens)):
            if type(self.tokens[i]) == int:
                expression.push(self.tokens[i])
            elif self.tokens[i] in ["/","*","+","-"]:
                if aux.peek() in ["/","*","+","-"]:
                    if check_priority(self.tokens[i],aux.peek()):
                        aux.push(self.tokens[i])
                    else:
                        while (check_priority(self.tokens[i],aux.peek())) == False:
                            temp = aux.peek()
                            if temp == "(" or temp == "{" or temp == "[":
                                aux.pop()
                                break
                            aux.pop()
                            expression.push(temp)
                        aux.push(self.tokens[i])
                else:
                    aux.push(self.tokens[i])
            elif self.tokens[i] == "(" or self.tokens[i] == "{" or self.tokens[i] == "[":
                aux.push(self.tokens[i])
            else:
                f = 0
                if self.tokens[i] == ")":
                    f = 1
                    while self.tokens[i] != "(":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "}":
                    while self.tokens[i] != "{":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "]":
                    while self.tokens[i] != "[":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                if f==1:
                    aux.pop()
        while aux.is_empty() == False:
            temp = aux.peek()
            aux.pop()
            expression.push(temp)
        # Evaluating the postfix expression
        try:
            spare = Stack()
            exp = Stack()
            for i in range(len(expression)):
                z = expression.peek()
                expression.pop()
                exp.push(z)
#postfix to infix correct!
#solving the postfix expression
            i = 0
            while exp.is_empty() == False:
                while exp.peek() not in ["+","-","/","*"]:
                    y = exp.peek()
                    exp.pop()
                    spare.push(y)
                a = spare.peek()
                spare.pop()
                b = spare.peek()
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
        if self.check_brackets(self.tokens):
            self.ans = self.evaluate_list_tokens(self.tokens)
        else:
            self.ans = "Error"
        self.hist.insert(0, (self.inp, self.ans))
        return self.ans

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples.
        The order is such that the most recently evaluated expression appears first.
        """
        return self.hist
    
# inst = AdvancedCalculator()
# print(inst.evaluate_expression("< write your expression here >"))


from simple_calculator import SimpleCalculator
from stack import Stack
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
        temp = self.inp.strip().split()
        for i in range(len(temp)):
            if ord(temp[i]) >= 48 and ord(temp[i]) <= 57:
                temp[i] = int(temp[i])
        return temp

    def check_brackets(self, list_tokens):
        """
        Check if brackets are valid, that is, all open brackets are closed by the same type 
        of brackets. Also, () contains only () brackets.
        Return True if brackets are valid, False otherwise.
        """
        for i in range(len(self.tokens)):
            if ord(self.tokens[i]) == 40:
                self.count_open1 += 1
            elif ord(self.tokens[i]) == 41:
                self.count_close1 += 1
            elif ord(self.tokens[i]) == 123:
                self.count_open2 += 1
            elif ord(self.tokens[i]) == 125:
                self.count_close2 += 1
            elif ord(self.tokens[i]) == 91:
                self.count_open3 += 1
            elif ord(self.tokens[i]) == 93:
                self.count_close3 += 1
        if (self.count_open1 == self.count_close1 and self.count_open2 == self.count_close2 and self.count_open3 == self.count_close3):
            return True
        else:
            return False

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
            order = ["/","*","+","-"]
            if order.index(oper1) < order.index(oper2):
                return True
            else:
                return False
        # infix to postfix 
        aux = Stack()
        expression = Stack()
        for i in range(len(self.tokens)):
            if (ord(self.tokens[i]) >= 48 and ord(self.tokens[i] <= 57)):
                expression.push(self.tokens[i])
            elif ord(self.tokens[i]) == 42 or ord(self.tokens[i]) == 43 or ord(self.tokens[i]) == 45 or ord(self.tokens[i]) == 47:
                if check_priority(self.tokens[i],aux.peek()):
                    aux.push(self.tokens[i])
                else:
                    while (check_priority(self.tokens[i],aux.peek())) == False:
                        temp = aux.peek()
                        if temp == "(" or temp == "{" or temp == "[":
                            break
                        aux.pop()
                        expression.push(temp)
                    aux.push(self.tokens[i])
            elif self.tokens[i] == "(" or self.tokens[i] == "{" or self.tokens[i] == "[":
                aux.push(self.tokens[i])
            else:
                if self.tokens[i] == ")":
                    while self.tokens[i] != "(":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "}":
                    while self.tokens[i] != "{":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                elif self.tokens[i] == "]":
                    while self.tokens[i] != "[":
                        temp = aux.peek()
                        aux.pop()
                        expression.push(temp)
                aux.pop()
        while aux.isempty() == False:
            temp = aux.peek()
            aux.pop()
            expression.push(temp)

        # Evaluating the postfix expression
        try:
            spare = Stack()
            exp = Stack()
            for i in range(len(expression)):
                z = expression.peek()
                expression.pop()
                exp.push(z)
            i = 0
            while exp.isempty == False:
                while exp.peek() not in ["+","-","/","*"]:
                    y = exp.peek()
                    exp.pop()
                    spare.push(y)
                a = spare.peek()
                spare.pop()
                b = spare.peek()
                spare.pop()
                op = exp.peek()
                exp.pop()
                spare.push(evaluate(a,b,op))
            self.ans = spare.peek()
            spare.push()
            if spare.isempty == False:
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
        if self.check_brackets(self.tokens):
            self.ans = self.evaluate_list_tokens(self.tokens)
        else:
            self.ans = "Error"
        self.hist.insert(0, (self.inp, self.ans))
        return self.ans

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples.
        The order is such that the most recently evaluated expression appears first.
        """
        return self.hist