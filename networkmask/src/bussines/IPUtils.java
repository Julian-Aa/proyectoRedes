/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bussines;

import static java.lang.Math.floor;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author rsvmedx
 */
public class IPUtils {
    private static int int_int[]=new int[4];
    private static String bin_int[]=new String[4],oct_int[]=new String[4],hex_int[]=new String[4];
    private static String mask[]=new String[4];
    public static String padLeft(String s, int n) {
        String out= String.format("%" + n + "s", s);
        out=out.replace(" ","0" );
        return out;
    }
    public static int[] get_int_ip(String ip){
        if (IPUtils.validateIP(ip)){
            String[] oct = ip.split(Pattern.quote("."));
            for (int i=0;i<=3;i++){
               int_int[i]= Integer.parseInt(oct[i]);
            }
        }
        return int_int;
    }
    public static String[] get_bin_ip(String ip){
        if (IPUtils.validateIP(ip)){
            String[] oct = ip.split(Pattern.quote("."));
            for (int i=0;i<=3;i++){
               int_int[i]= Integer.parseInt(oct[i]); 
               bin_int[i]= padLeft(Integer.toBinaryString(int_int[i]),8);
            }
        }
        return bin_int;
    } 
    public static String[] get_oct_int(String ip){
        if (IPUtils.validateIP(ip)){
            String[] oct = ip.split(Pattern.quote("."));
            for (int i=0;i<=3;i++){
               oct_int[i]= Integer.toOctalString(int_int[i]);
            }
        }
        return oct_int;
    }   
    public static String[] get_hex_int(String ip){
        if (IPUtils.validateIP(ip)){
            String[] oct = ip.split(Pattern.quote("."));
            for (int i=0;i<=3;i++){
               hex_int[i]= Integer.toHexString((int_int[i]));
            }
        }
        return hex_int;
    }
    public static boolean validateIP(String ip){
        String regex = "^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ip);
        boolean result=matcher.matches();
        return result;
    }
    public static int[] getMask(int prefijo){
        String[] mask=new String[32];
        String s;
        int decimal;
        
        Arrays.fill(mask, "0");
        for (int i=0;i<=prefijo-1;i++){
            mask[i]="1"; 
        }

        //octeto 1
        s="";
        for (int i=0;i<=7;i++){
            s=s+mask[i]; 
        }
        decimal=Integer.parseInt(s,2);  
        int_int[0]=decimal;
        
        //octeto 2
        s="";
        for (int i=8;i<=15;i++){
            s=s+mask[i]; 
        }
        decimal=Integer.parseInt(s,2);  
        int_int[1]=decimal;
        
        //octeto 3
        s="";
        for (int i=16;i<=23;i++){
            s=s+mask[i]; 
        }
        decimal=Integer.parseInt(s,2);  
        int_int[2]=decimal;
        
        //octeto 4
        s="";
        for (int i=24;i<=31;i++){
            s=s+mask[i]; 
        }
        decimal=Integer.parseInt(s,2);  
        int_int[3]=decimal;
        
        return int_int;
    }   
}
