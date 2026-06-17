import java.util.Scanner;

class NumberPrinter {
    int n;
    int count = 1;

    NumberPrinter(int n) {
        this.n = n;
    }

    public synchronized void printOdd() {
        while (count <= n) {
            while (count % 2 == 0) {
                try {
                    wait();
                } catch (Exception e) {
                }
            }
            if (count <= n) {
                System.out.print(count + " ");
                count++;
                notify();
            }
        }
    }

    public synchronized void printEven() {
        while (count <= n) {
            while (count % 2 == 1) {
                try {
                    wait();
                } catch (Exception e) {
                }
            }
            if (count <= n) {
                System.out.print(count + " ");
                count++;
                notify();
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        NumberPrinter np = new NumberPrinter(n);

        Thread t1 = new Thread(() -> np.printOdd());
        Thread t2 = new Thread(() -> np.printEven());

        t1.start();
        t2.start();
    }
}
