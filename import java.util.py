import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ATM {
    private Map<String, Integer> accounts; // Stores account numbers and their balances

    public ATM() {
        accounts = new HashMap<>();
        // Predefined accounts for demo purposes
        accounts.put("12345", 1000); // Account number: Balance
        accounts.put("67890", 2000);
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        String accountNumber;

        System.out.println("Welcome to the ATM!");
        System.out.print("Please enter your account number: ");
        accountNumber = scanner.nextLine();

        if (!accounts.containsKey(accountNumber)) {
            System.out.println("Invalid account number. Exiting.");
            return;
        }

        int choice;
        do {
            System.out.println("\nATM Menu:");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    checkBalance(accountNumber);
                    break;
                case 2:
                    depositMoney(accountNumber, scanner);
                    break;
                case 3:
                    withdrawMoney(accountNumber, scanner);
                    break;
                case 4:
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);

        scanner.close();
    }

    private void checkBalance(String accountNumber) {
        System.out.println("Your balance is: $" + accounts.get(accountNumber));
    }

    private void depositMoney(String accountNumber, Scanner scanner) {
        System.out.print("Enter amount to deposit: $");
        int amount = scanner.nextInt();
        if (amount > 0) {
            accounts.put(accountNumber, accounts.get(accountNumber) + amount);
            System.out.println("Successfully deposited $" + amount);
        } else {
            System.out.println("Invalid amount. Please enter a positive number.");
        }
    }

    private void withdrawMoney(String accountNumber, Scanner scanner) {
        System.out.print("Enter amount to withdraw: $");
        int amount = scanner.nextInt();
        int balance = accounts.get(accountNumber);
        if (amount > 0 && amount <= balance) {
            accounts.put(accountNumber, balance - amount);
            System.out.println("Successfully withdrew $" + amount);
        } else if (amount > balance) {
            System.out.println("Insufficient funds. Your balance is $" + balance);
        } else {
            System.out.println("Invalid amount. Please enter a positive number.");
        }
    }

    public static void main(String[] args) {
        ATM atm = new ATM();
        atm.run();
    }
}
