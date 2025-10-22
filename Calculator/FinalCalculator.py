import InfixToPostfix, CalculatePostfix

user_input = input()
postfix = InfixToPostfix.infix_to_postfix(user_input)
ans = CalculatePostfix.calculate_postfix(postfix)
print(ans)