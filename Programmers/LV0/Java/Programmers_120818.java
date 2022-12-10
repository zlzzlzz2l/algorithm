import java.math.BigDecimal;

public class Programmers_120818 {
    public static void main(String[] args) {
        Programmers_120818 s = new Programmers_120818();

        int price = 90000;

        System.out.println(s.solution(price));
    }

    public int solution(int price) {
        double sale = 1.0;

        if (price >= 100000 && price <= 299999) {
            sale = 0.95;
        } else if (price >= 300000 && price <= 499999) {
            sale = 0.9;
        } else if (price >= 500000) {
            sale = 0.8;
        } else {
            sale = 1.0;
        }

        double total = price * sale;

        return (int) total;
    }
}
