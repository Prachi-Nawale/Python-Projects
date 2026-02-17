import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv("expenses.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return df


def show_summary(df):
    print("\n========== EXPENSE DASHBOARD ==========")
    print(f"Total Expense: ₹{df['amount'].sum()}")

    category_totals = df.groupby("category")["amount"].sum()
    print("\nCategory Wise Expense:")
    print(category_totals)

    top_category = category_totals.idxmax()
    print(f"\nHighest Spending Category: {top_category}")
    print("========================================\n")


def show_pie_chart(df):
    category_totals = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(8, 8))
    category_totals.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Expense Distribution by Category", fontsize=14)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("category_distribution.png")  # Auto save
    plt.show()


def show_monthly_trend(df):
    monthly_totals = df.groupby("month")["amount"].sum()

    plt.figure(figsize=(10, 5))
    monthly_totals.plot(marker="o")
    plt.title("Monthly Expense Trend", fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("monthly_trend.png")  # Auto save
    plt.show()


def show_bar_chart(df):
    category_totals = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(10, 5))
    category_totals.plot(kind="bar")
    plt.title("Category Wise Expenses", fontsize=14)
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig("category_bar_chart.png")  # Auto save
    plt.show()


def main():
    df = load_data()
    show_summary(df)
    show_bar_chart(df)
    show_pie_chart(df)
    show_monthly_trend(df)


if __name__ == "__main__":
    main()
