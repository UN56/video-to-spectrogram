import os
import cv2

def convert_frames_to_video(input_list,output_file_name,fps,size):

    ## you
    num_frames = 3237
    ##
    # Define the output video writer object 
    out = cv2.VideoWriter(output_file_name, fourcc, fps, size)

    for i in range(num_frames):
        # base_name='img'
        img_name = 'videoFrames\\'+'{:04d}'.format(i) + '.jpeg'
        
        try:
            img = cv2.imread(img_name)
            out.write(img) # Write out frame to video
        except:
            print(img_name + ' does not exist')
        
        if img is not None:
            cv2.imshow('img',img)
            cv2.waitKey(1)
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    print("The output video is {} is saved".format(output_file_name))

if __name__=='__main__':
    
    path = os.getcwd()

    data_subdir = 'output'

    img_list = os.listdir(path)

    frame = cv2.imread(os.path.join(path,'0000.jpeg')) 
    fps = 15
    output_file_name = 'output.mp4'.format(data_subdir,fps)
    # Define the codec.FourCC is a 4-byte code used to specify the video codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    size = (852,480)
    convert_frames_to_video(img_list,output_file_name,fps,size)