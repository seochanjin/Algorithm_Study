import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] groups = br.readLine().split("-");

        int result = 0;

        for(int i = 0; i < groups.length; i++){
            int tempSum = calculateSum(groups[i]);

            if(i == 0){
                result += tempSum;
            } else {
                result -= tempSum;
            }
        }

        System.out.println(result);
    }

    private static int calculateSum(String group) {
        int sum = 0;
        String[] numbers = group.split("\\+");
        for (String num : numbers) {
            sum += Integer.parseInt(num);
        }
        return sum;
    }
}