# README.md

## Another Expense Tracker

Another Expense Tracker is a personal finance management tool that helps users track their expenses and manage their budget. This project is built with a focus on simplicity and ease of use, allowing users to quickly add, edit, and delete expenses, as well as view their spending habits in various categories over time.

## Features

- Add, edit, and delete expenses
- Categorize expenses
- Visualize spending habits in a pie chart
- Filter expenses by date range and category
- Export data to CSV for further analysis
- Responsive design for mobile and desktop devices

## Getting Started

### Prerequisites

- Node.js (>= 14.x.x)
- npm (>= 6.x.x)
- MongoDB (>= 4.x.x)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sonnymay/another-expense-tracker.git
   cd another-expense-tracker
   ```

2. Install the dependencies:

   ```
   npm install
   ```

3. Create a `.env` file in the root directory of the project and set up the following environment variables:

   ```
   MONGODB_URI=<Your MongoDB connection string>
   ```

4. Start the development server:

   ```
   npm run dev
   ```

5. Open your web browser and navigate to `http://localhost:3000`.

## Usage

1. Click on the "Add Expense" button to add a new expense.
2. Fill in the required fields and click "Save" to store the expense.
3. Click on the expense item in the list to edit or delete it.
4. Use the filters at the top of the page to filter expenses by date range and category.
5. View the pie chart to visualize your spending habits in different categories.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
