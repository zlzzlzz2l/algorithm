public class Programmers_120817 {
    public static void main(String[] args) {
        Programmers_120817 s = new Programmers_120817();

        int[] numbers = {89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};

        System.out.println(s.solution(numbers));
    }

    public double solution(int[] numbers) {
        double answer = 0;

        for (int number : numbers) {
            answer += number;
        }

        answer = answer / numbers.length;

        return answer;
    }
}
