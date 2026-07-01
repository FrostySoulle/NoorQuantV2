from research import analyze_factor

result = analyze_factor(
    days=60,
    factor="RS_60"
)

print(result["Winner"])