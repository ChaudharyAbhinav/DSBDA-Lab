
        import java.io.File;
        import java.io.FileNotFoundException;
        import java.util.Arrays;
        import java.util.Scanner;

public class fileread {
    public static void main(String[] args) {
        try {
            File Obj = new File("/Users/abhi/Desktop/abcd/part-r-00000");
            Scanner Reader = new Scanner(Obj);
            String key = "";
            int max = 0;

            while (Reader.hasNextLine()) {
                String data = Reader.nextLine();
                String[] vals = data.split("	");
//                System.out.println(Arrays.toString(vals));
                int count = Integer.parseInt(vals[1]);
                if (count > max) {
                    key = vals[0];
                    max = count;
                }
            }
            System.out.println(key + " -> " + max);
            Reader.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("An error has occurred.");
            e.printStackTrace();
        }
    }
}