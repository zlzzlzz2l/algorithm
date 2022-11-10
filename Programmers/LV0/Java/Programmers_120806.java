public class Programmers_120806 {
    public static void main(String[] args) {
        Programmers_120806 s = new Programmers_120806();

        int num1 = 3;
        int num2 = 2;

        System.out.println(s.solution(num1, num2));
    }

    public int solution(int num1, int num2) {
        double answer = 0.0;
        answer = (double)num1 / (double)num2;
        answer *= 1000;
        return (int)answer;
    }
}
