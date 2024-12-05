This repository contains examples demonstrating a common Python error: RecursionError. The bug.py file shows a recursive function that works for small inputs but fails for larger ones due to exceeding the recursion depth. The bugSolution.py file offers a solution using iteration to avoid the recursion depth limitation.  The error arises because Python has a default recursion depth limit to prevent stack overflow. This limit can be adjusted, but using iteration is generally a more robust and efficient approach for tasks that could be solved recursively.