success_ratio = 0.6

reward = (
    1828.57 * (success_ratio ** 3)
    - 3733.33 * (success_ratio ** 2)
    + 2800 * success_ratio
    - 595.24
)

print(f"{reward}")
print(f"{success_ratio}")

