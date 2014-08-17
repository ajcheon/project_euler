import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;
 
 
public class Buutton extends Applet implements Runnable, ActionListener
{
//     Multiple scanners to read different texts/files
    Scanner kb;
    Scanner tr;
    Scanner lr;
 
//     Multiple strings for storage
    String fromtext; //lines from the script
    String printedout; //actual dialogue/text stuff that is printed in main textbox
    String n; //name that is printed with text (i.e. "Ai") in the mini textbox
    String type; //records where inputed picture is supposed to go
    String points; //keeps track of who the points should be added to
 
//     Images for background, middle, foreground8
    Image backImage;
    Image midImage;
    Image foreImage;
 
//     The options written on the buttons
    String b11;
    String b22;
    String b33;
    String b44;
    String b55;
    String b66;
    String b77;
    String b88;
 
//     Buttons for choosing options
    Button b1;
    Button b2;
    Button b3;
    Button b4;
    Button b5;
    Button b6;
    Button b7;
    Button b8;
 
//     Counters to keep track of affection points
    int j; //jun
    int s; //shohei
    int m; //makoto
    int r; //ryuu
    int k; //keiji
 
    public void init()
    {
       setBackground(Color.blue);
 
//        Set first scanner to read script
       try{
           kb = new Scanner(new File("order2.txt"));}
       catch(java.io.IOException e){
           System.out.println("Cannot access text.txt");}
 
       setFont(new Font("Times New Roman", Font.PLAIN, 24));
       printedout = "";
       setSize(800, 600);
    }
 
    public void start(){}
 
    public void stop(){}
 
    public void destroy(){}
 
    public boolean mouseDown(Event e, int x, int y)
    {
//         Makes sure that when button options are up, player cannot click randomly to go to next dialogue
        if (printedout.equals("...")) //Ai says "..." whenever there are options up
        return false;
 
//         Reads line from script
        fromtext = kb.nextLine();
 
        //special case scene where player picks between our smexy guys
        if(fromtext.equals("lastlast.txt"))
        {
            lastlast();
        }
 
//         Makes buttons when called upon from script
        else if (fromtext.substring(0, 6).equals("button"))
        {
            makebutttons(fromtext);
        }
 
//         Sets pictures (backgrounds, middle, foreground)
        else if (fromtext.substring(fromtext.length()-7, fromtext.length()-4).equals("gif"))
        {
            printedout = ""; //make sure no text is printed to make clean transition
            n = "";
            setPicture(fromtext);
        }
 
//         Sets text to print out
        else
        {
            setNameandText(fromtext);
        }
        repaint();
        return true;
    }
 
    public void run(){}
 
    public void actionPerformed(ActionEvent e)
    {
//         Determines which lines to read from the specified button text file depending on the button pressed
        if (e.getActionCommand().equals(b11)) //if you press the first button...
        {
            setPicture(tr.nextLine()); //read the first line of the text file for the picture of the character you're talking to
            setNameandText(tr.nextLine()); //read second line for what they say
            for(int i=0;i
            tr.nextLine(); //skip lines that are not used to the...
            addPoints(points,tr.nextInt()); //points corresponding to the response
        }
        else if (e.getActionCommand().equals(b22)) //if you press the second button...
        {
            for(int i=0;i
            tr.nextLine();
            setPicture(tr.nextLine()); //to the second one.
            setNameandText(tr.nextLine());
            for(int i=0;i<3;i++)
            tr.nextLine(); //skip lines again...
            addPoints(points,tr.nextInt()); //to the points
        }
        else if (e.getActionCommand().equals(b33)) //etc.
        {
            for(int i=0;i
            tr.nextLine();
            setPicture(tr.nextLine());
            setNameandText(tr.nextLine());
            for(int i=0;i
            tr.nextLine();
            addPoints(points,tr.nextInt());
        }
//         special cases for lastlast() when there are five buttons
        else
        {
            setPicture("textbox.gif.for");
            setNameandText(tr.nextLine()); //Ai's confession
            if (e.getActionCommand().equals(b44)) //shohei's button
            {
                if (s>=5) //if you rack up enough points, you get the good stuff
                {
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
                else //if not, straight rejection. BUAHAHAHA.
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
            }
            else if (e.getActionCommand().equals(b55)) //jun
            {
                if (j>=5)
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
                else
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
            }
            else if (e.getActionCommand().equals(b66)) //ryuu
            {
                if (r>=5)
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
                else
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
            }
            else if (e.getActionCommand().equals(b77)) //keiji
            {
                if (k>=5)
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
                else
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
            }
            else
            {
                if (m>=5) //makoto
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
                else
                {
                    for(int i=0;i
                    tr.nextLine();
                    setPicture(tr.nextLine());
                    setNameandText(tr.nextLine());
                }
            }
            remove(b4);
            remove(b5);
            remove(b6);
            remove(b7);
            remove(b8);
        }
        setPicture("textbox.gif.for"); //after setting the mid images, you have to set another textbox
        //because of the postconditions in the method setPicture()
 
//         removes buttons after they are clicked
        remove();
        repaint();
    }
 
 
//     paint images and text
    public void paint (Graphics g) //draws layers
    {
       g.drawImage(backImage, 0, 0, this);
       g.drawImage(midImage, 0, 0, this);
       g.drawImage(foreImage, 0, 0, this);
       g.drawString(n, 80, 440);
       g.drawString(printedout, 80, 500);
    }
 
//     We would have used this, but it was being funky.
//     public void update (Graphics g)
//     {
//        paint(g);
//     }
 
//     Removes regular buttons
    private void remove()
    {
        remove(b1);
        remove(b2);
        remove(b3);
    }
 
//     Method used to determine whether the picture belongs in the back, mid, or foreground
//     We thought we would use this more, but we ended up only using it...once?
    private String decode(String str)
    {
        return str.substring(str.length()-3);
    }
 
//     Method used to set string variables that are printed out
    private void setNameandText(String x)
    {
        lr = new Scanner(x); //set third scanner to read line to use next() method...
        n = lr.next(); //which should read the name of the person who is talking
        if (n.equals(":"))
        n = "";
        printedout = lr.nextLine(); //records the rest of the line for dialogue
    }
 
//     method used to set all the pictures
    private void setPicture(String pic)
    {
        type = decode(pic); //either bck, mid, or for at the end of the string to determine which layer the picture is
        String what = pic.substring(0, pic.length()-4); //name of the .gif file
        if (type.equals("bck")) //background
        {
            backImage = getImage(getCodeBase(), what);
            midImage = null; //other images are removed for clean transition
            foreImage = null;
        }
        else if (type.equals("mid")) //middle
        {
            midImage = getImage(getCodeBase(), what);
            foreImage = null;
        }
        else if (type.equals("for")) //foreground
            foreImage = getImage(getCodeBase(), what);
    }
 
//     method used to add affection points to each character
    private void addPoints(String name, int score)
    {
        if (name.equals("m")) //makoto
        m+=score;
        else if (name.equals("j")) //jun
        j+=score;
        else if (name.equals("s")) //shohei
        s+=score;
        else if (name.equals("k")) //keiji
        k+=score;
        else //ryuu
        r+=score;
    }
 
//     makes regular buttons
    private void makebutttons(String poop) //poop is the name of the specific button file that will be read
    {
        try{
            tr = new Scanner(new File(poop));}
        catch(java.io.IOException ex){
            System.out.println("Cannot access text.txt");}
        points = tr.nextLine(); //first line of the text is the name of the character that you're interacting with
 
        //set button choices from next three lines
        b11 = tr.nextLine();
        b22 = tr.nextLine();
        b33 = tr.nextLine();
 
        b1 = new Button(b11);
        b1.setActionCommand(b11);
        b1.setBounds(100, 300, 600, 40);
        b1.addActionListener(this);
 
        b2 = new Button(b22);
        b2.setActionCommand(b22);
        b2.setBounds(100, 350, 600, 40);
        b2.addActionListener(this);
 
        b3 = new Button(b33);
        b3.setActionCommand(b33);
        b3.setBounds(100, 400, 600, 40);
        b3.addActionListener(this);
 
        //add buttons to applet screen
        add(b1);
        add(b2);
        add(b3);
 
        printedout = "...";
        n = "";
    }
 
//     special case for the last scene where you choose between the five guys
    private void lastlast()
    {
        try{
            tr = new Scanner(new File("lastlast.txt"));}
        catch(java.io.IOException ex){
            System.out.println("Cannot access text.txt");}
 
//         Messed up here, so it's out of order. Sorry.
        b66 = "Ryuu";
        b77 = "Keiji";
        b88 = "Makoto";
        b44 = "Shohei";
        b55 = "Jun";
 
        b6 = new Button(b66);
        b6.setActionCommand(b66);
        b6.setBounds(100, 300, 600, 40);
        b6.addActionListener(this);
 
        b7 = new Button(b77);
        b7.setActionCommand(b77);
        b7.setBounds(100, 350, 600, 40);
        b7.addActionListener(this);
 
        b8 = new Button(b88);
        b8.setActionCommand(b88);
        b8.setBounds(100, 400, 600, 40);
        b8.addActionListener(this);
 
        b4 = new Button(b44);
        b4.setActionCommand(b44);
        b4.setBounds(100, 250, 600, 40);
        b4.addActionListener(this);
 
        b5 = new Button(b55);
        b5.setActionCommand(b55);
        b5.setBounds(100, 200, 600, 40);
        b5.addActionListener(this);
 
        add(b4);
        add(b5);
        add(b6);
        add(b7);
        add(b8);
 
        printedout = "...";
        n = "";
    }
}