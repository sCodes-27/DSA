class Solution(object):
    def removeOccurrences(self, s, part):

        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= len(part):
                if ''.join(stack[-len(part):]) == part:
                    del stack[-len(part):]

        return ''.join(stack)