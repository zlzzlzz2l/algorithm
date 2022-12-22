public class Programmers_120837 {
    public static void main(String[] args) {
        Programmers_120837 s = new Programmers_120837();

        int hp = 999;

        System.out.println(s.solution(hp));
    }

    public int solution(int hp) {
        int answer = 0;

        while (hp != 0) {
            if (hp >= 5) {
                answer += hp / 5;
                hp = hp % 5;
            }
            else if (hp >= 3) {
                answer += hp / 3;
                hp = hp % 3;
            }
            else {
                answer += hp;
                hp = 0;
            }
        }

        return answer;
    }
}
