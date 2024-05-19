import os

# Path to the directory containing your paired-end read files
directory = '.'

# List all files in the directory
files = os.listdir(directory)

# Filter out forward read files
forward_reads = [f for f in files if '_1.fastq' in f]

# Create a manifest file
with open('manifest.tsv', 'w') as manifest:
    # Write the header using tabs as separators
    manifest.write('sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n')
    
    # Loop through the forward read files and write entries for both forward and reverse reads
    for forward_read in forward_reads:
        sample_id = forward_read.split('_1.fastq')[0]  # Extract sample ID from the file name
        forward_filepath = os.path.abspath(os.path.join(directory, forward_read))
        reverse_filepath = os.path.abspath(os.path.join(directory, forward_read.replace('_1.fastq', '_2.fastq')))
        
        # Write the entry using tabs as separators
        manifest.write(f'{sample_id}\t{forward_filepath}\t{reverse_filepath}\n')
