from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                # Build the substring inside the brackets
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # Remove the '['
                stack.pop()

                # Get the repeat count
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # Push the decoded substring back onto the stack
                stack.append(int(num) * substr)

        return "".join(stack)