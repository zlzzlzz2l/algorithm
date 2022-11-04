public class Programmers_120805 {
    public static void main(String[] args) {
        Programmers_120805 s = new Programmers_120805();

        int num1 = 4;
        int num2 = 2;

        System.out.println(s.solution(num1, num2));
    }

    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 / num2;
        return answer;
    }
}
