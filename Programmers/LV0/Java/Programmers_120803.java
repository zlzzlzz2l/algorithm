public class Programmers_120803 {
    public static void main(String[] args) {
        Programmers_120803 s = new Programmers_120803();

        int num1 = 10;
        int num2 = 5;

        System.out.println(s.solution(num1, num2));
    }

    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 - num2;
        return answer;
    }
}
