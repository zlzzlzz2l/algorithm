public class Programmers_120810 {

    public static void main(String[] args) {

        Programmers_120810 s = new Programmers_120810();

        int num1 = 5;
        int num2 = 3;

        System.out.println(s.solution(num1, num2));
    }

    public int solution(int num1, int num2) {
        int answer = -1;
        answer = num1 % num2;
        return answer;
    }
}