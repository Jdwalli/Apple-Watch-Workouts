import React from "react";

interface Props {
  variant: 'primary' | 'secondary' | 'disabled';
  type?: 'button' | 'submit' | 'reset' | undefined;
  text: string;
  className?: string;
  disabled?: boolean;
  onClick?: () => void;
}

const primaryStyles =
  'text-sm text-white font-semibold bg-green-600 px-5 py-2 mx-2 rounded';
const secondaryStyles =
  'text-sm text-white font-semibold bg-purple-600 px-5 py-2 mx-2 rounded';
const disabled =
  'text-sm text-shark-400 bg-shark-100 px-5 py-2 mx-2 rounded opacity-70 cursor-not-allowed';

  const styles = {
    primary: primaryStyles,
    secondary: secondaryStyles,
    disabled: disabled,
  };

const Button: React.FC<Props> = (props: Props) => {
  const classes = `btn ${styles[props.variant]} ${props.className ? props.className : ''}`;
  const type = props.type ? props.type : 'button';

  return (
    <button
      className={classes}
      onClick={props.onClick}
      type={type}
      disabled={props.disabled ?? false}
    >
      {props.text}
    </button>
  );
};

export default Button;