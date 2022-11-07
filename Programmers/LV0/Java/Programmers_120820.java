public class Programmers_120820 {
    public static void main(String[] args) {
        Programmers_120820 s = new Programmers_120820();

        int age = 40;

        System.out.println(s.solution(age));
    }

    public int solution(int age) {
        int answer = 0;
        answer = 2022 - age + 1;
        return answer;
    }
}
