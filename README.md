# CrossSeq

<p align="center">
  <img width="300" height="300" src="https://raw.githubusercontent.com/AhmetMuratAcar/CrossSeq/master/Images/Logo.png">
</p>

## What is CrossSeq
CrossSeq is a simple visualization tool for comparing and contrasting the coding regions of mRNA FASTA sequences. One main sequence is chosen and any number of comparison sequences can be added. These comparison sequences are then compared to the main sequence in both nucleotide and codon analysis. It is important to note that this comparison is done in a 1:1 fashion. Therefore, problems such as frameshift mutations are not taken into consideration.

The resulting analysis yields 2 graphs and a markdown file containing the generated statistics per comparison sequence. 

## How to Install and Run CrossSeq
Ensure that you have a version of Python > 3.7 installed. Clone this repository to your device. Access the local file through your terminal and run the following command to install the dependencies:
```
pip install -r requirements.txt
```
After the dependencies are successfully installed, all you need to do is run the `App.py` file.

## Navigating the UI

### New Sequence Button
  - This button creates a new text box under the last one in the Sequence List.

### Sequence Names
  - The names of sequences in the Sequence List on the right side of the application are actually buttons. Clicking the names creates a popout window containing the textbox and its contents for that name. Any edits done in this popout window will update its respective textbox on the main window in real time. Note that only one popout window can be active at a time.

### Trash Buttons
  - Each text box has its own trash button which is used for deleting its contents. If any text is in the textbox, clicking the trash button will delete said contents. If no text is present in the textbox, clicking the trash button will delete that textbox and update the Sequence List accordingly. 

### Theme Dropdown
  - The defult theme for this application is your system's theme. However using the dropdown under the "Submit" button you can switch between the light or dark themes.

## Example Usage
The following screenshots illustrate how to use CrossSeq using the 4 FASTA sequences provided in the [Testing Sequences](https://github.com/AhmetMuratAcar/CrossSeq/tree/master/Testing%20Sequences) folder.

<p align="center">
  <img src="https://github.com/AhmetMuratAcar/CrossSeq/blob/master/Images/Example%20Run/Initial_Comparison.png?raw=true">
</p>

After adding all of the sequences simply click the "Submit" button to get the following results:

<p align="center">
  <img src="https://github.com/AhmetMuratAcar/CrossSeq/blob/master/Images/Example%20Run/Results_Page.png?raw=true">
</p>

Finally, click the "Download Results" button and choose your desired location. The results should be downloaded in the following format:

<p align="center">
  <img src="https://github.com/AhmetMuratAcar/CrossSeq/blob/master/Images/Example%20Run/Downloaded_Folder.png?raw=true">
</p>

This is what the generated Markdown file should look like:

<p align="center">
  <img src="https://github.com/AhmetMuratAcar/CrossSeq/blob/master/Images/Example%20Run/Results_MD.png?raw=true">
</p>

*Note that this image only shows the results of the first comparison sequence.
