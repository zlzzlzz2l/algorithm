import java.util.ArrayList;

public class Programmers_120819 {
    public static void main(String[] args) {
        Programmers_120819 s = new Programmers_120819();

        int money = 15000;

        System.out.println(s.solution(money));
    }

    public ArrayList<Integer> solution(int money) {
        ArrayList<Integer> answer = new ArrayList<>();

        int cup = money / 5500;
        int coin = money % 5500;

        answer.add(cup);
        answer.add(coin);

        return answer;
    }
}
