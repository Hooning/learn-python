# String membership operators: in, not in
print("a" in "cat")
print("f" not in "python")

# List membership operators: in, not in
print(3 in [1, 2, 3, 4, 5])
print("cat" in ["cat", "dog", "mouse"])

# Security check: ensure the domain is not banned
domain = "google.com"  # User inputed domain
banned_domains = ["example.com", "test.com", "banned.com"]
print(f"Is {domain} banned?", domain in banned_domains)
