export const FormatNumberWithUnit = (value: number, unit: string) => {
    const CompactFormat = Intl.NumberFormat("en", { notation: "compact" });
    const formattedValue = CompactFormat.format(value);
    return `${formattedValue} ${unit}`;
};

export const FormatNumber = (value: number) => {
    const CompactFormat = Intl.NumberFormat("en", { notation: "compact" });
    return CompactFormat.format(value);
};

