import React from "react";

interface Props {
  variant: 'primary' | 'secondary' | 'disabled';
  type?: 'button' | 'submit' | 'reset' | undefined;
  text: string;
  className?: string;
  disabled?: boolean;
  onClick?: () => void;
}

const styles = {
  primary: 'bg-green-500 text-white font-bold py-2 px-4 rounded',
  secondary: 'bg-purple-500 text-white font-bold py-2 px-4 rounded',
  disabled: 'bg-gray-600 text-white font-bold py-2 px-4 rounded opacity-50 cursor-not-allowed',
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