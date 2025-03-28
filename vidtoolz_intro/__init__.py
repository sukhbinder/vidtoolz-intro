import vidtoolz
import os
from moviepy import concatenate_videoclips, VideoFileClip


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_intro.mp4")


def process_video_clips(input_data):

    video_clips = []
    if isinstance(input_data, str):
        lines = input_data.strip().split("\n")
    else:
        lines = input_data

    # Parse the input data into a list of tuples (video_name, start_time, end_time)
    for line in lines:
        print(line)
        parts = line.split(",")
        if len(parts) != 3:
            raise ValueError(f"Invalid input format: {line}")

        video_name = parts[0].strip()
        start_time = float(parts[1].strip())
        end_time = float(parts[2].strip()) if parts[2].strip().isdigit() else None

        # Load the video and clip it
        clip = VideoFileClip(video_name)
        if end_time is not None:
            clip = clip.subclipped(start_time, end_time)
        else:
            clip = clip.subclipped(start_time)

        video_clips.append(clip)

    # Concatenate all clips together
    final_clip = concatenate_videoclips(video_clips)

    return final_clip


def write_file(final_clip, output):
    # Write the output to a new file
    final_clip.write_videofile(output, codec="libx264", audio_codec="aac")


def create_parser(subparser):
    parser = subparser.add_parser(
        "intro", description="Create intro video from a series of videos"
    )
    parser.add_argument(
        "-t",
        "--textfile",
        type=str,
        default=None,
        help="Text file containg. IMG102.mov,1,5\n IMG200.mov,2,4",
    )
    parser.add_argument(
        "-i", "--input", type=str, action="append", help="Input like  IMG102.mov,1,5"
    )
    parser.add_argument(
        "-o", "--output", type=str, default=None, help="Output filename, default None"
    )


class ViztoolzPlugin:
    """Create intro video from a series of videos"""

    __name__ = "intro"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.hello)

    def run(self, args):
        output = determine_output_path(args.input, args.output)
        if args.textfile:
            with open(args.textfile, "r") as fin:
                data = fin.read()
        elif args.input:
            data = args.input

        final_clip = process_video_clips(data)
        write_file(final_clip, output)

    def hello(self, args):
        # this routine will be called when "vidtoolz "intro is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


intro_plugin = ViztoolzPlugin()
